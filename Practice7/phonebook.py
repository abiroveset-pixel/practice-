import csv
from pathlib import Path
from connect import connect

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL
);
"""


def ensure_table_exists():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(CREATE_TABLE_SQL)


def print_contacts(rows):
    if not rows:
        print("No contacts found.")
        return

    print("\nID | Name | Phone")
    print("---|------|------")
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]}")


def insert_from_console():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()

    if not name or not phone:
        print("Name and phone are required.")
        return

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO phonebook(first_name, phone) VALUES (%s, %s)",
                (name, phone)
            )

    print("Contact added!")


def insert_from_csv(filename):
    csv_path = Path(filename)
    if not csv_path.exists():
        print(f"CSV file not found: {filename}")
        return

    inserted = 0
    skipped = 0

    with connect() as conn:
        with conn.cursor() as cur:
            with open(csv_path, newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) < 2:
                        skipped += 1
                        continue

                    first_name = row[0].strip()
                    phone = row[1].strip()
                    if not first_name or not phone:
                        skipped += 1
                        continue

                    cur.execute(
                        "INSERT INTO phonebook(first_name, phone) VALUES (%s, %s) ON CONFLICT(phone) DO NOTHING",
                        (first_name, phone)
                    )
                    if cur.rowcount > 0:
                        inserted += 1
                    else:
                        skipped += 1

    print(f"CSV import complete: {inserted} added, {skipped} skipped.")


def show_all():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook ORDER BY id")
            rows = cur.fetchall()
    print_contacts(rows)


def search_by_name():
    name = input("Enter name: ").strip()
    if not name:
        print("Enter a name or part of a name.")
        return

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM phonebook WHERE first_name ILIKE %s ORDER BY first_name",
                (f"%{name}%",)
            )
            rows = cur.fetchall()

    print_contacts(rows)


def search_by_phone():
    prefix = input("Phone prefix: ").strip()
    if not prefix:
        print("Enter a phone prefix.")
        return

    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM phonebook WHERE phone LIKE %s ORDER BY phone",
                (f"{prefix}%",)
            )
            rows = cur.fetchall()

    print_contacts(rows)


def update_contact():
    phone = input("Phone of contact to update: ").strip()
    if not phone:
        print("Phone is required.")
        return

    print("1. Change name")
    print("2. Change phone")
    choice = input("Choose action: ").strip()

    with connect() as conn:
        with conn.cursor() as cur:
            if choice == "1":
                new_name = input("New name: ").strip()
                if not new_name:
                    print("New name is required.")
                    return
                cur.execute(
                    "UPDATE phonebook SET first_name = %s WHERE phone = %s",
                    (new_name, phone)
                )
            elif choice == "2":
                new_phone = input("New phone: ").strip()
                if not new_phone:
                    print("New phone is required.")
                    return
                cur.execute(
                    "UPDATE phonebook SET phone = %s WHERE phone = %s",
                    (new_phone, phone)
                )
            else:
                print("Invalid choice.")
                return

            if cur.rowcount == 0:
                print("No contact found with that phone number.")
                return

    print("Contact updated!")


def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")
    choice = input("Choose action: ").strip()

    with connect() as conn:
        with conn.cursor() as cur:
            if choice == "1":
                name = input("Name: ").strip()
                if not name:
                    print("Name is required.")
                    return
                cur.execute(
                    "DELETE FROM phonebook WHERE first_name = %s",
                    (name,)
                )
            elif choice == "2":
                phone = input("Phone: ").strip()
                if not phone:
                    print("Phone is required.")
                    return
                cur.execute(
                    "DELETE FROM phonebook WHERE phone = %s",
                    (phone,)
                )
            else:
                print("Invalid choice.")
                return

            if cur.rowcount == 0:
                print("No matching contact was found.")
                return

    print("Contact deleted!")


def main():
    try:
        ensure_table_exists()
    except Exception as exc:
        print("Database connection failed.")
        print("Check config.py, your PostgreSQL credentials, or environment variables PGHOST/PGDATABASE/PGUSER/PGPASSWORD/PGPORT.")
        print(f"Error: {exc}")
        return

    while True:
        print("\nPHONEBOOK")
        print("1. Import CSV")
        print("2. Add contact")
        print("3. Show all")
        print("4. Search by name")
        print("5. Search by phone prefix")
        print("6. Update contact")
        print("7. Delete contact")
        print("8. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            insert_from_csv("contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            show_all()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            search_by_phone()
        elif choice == "6":
            update_contact()
        elif choice == "7":
            delete_contact()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 8.")


if __name__ == "__main__":
    main()