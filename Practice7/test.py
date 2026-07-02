import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="postgres",
        password="1234",
        port="5432"
    )
    print("CONNECTED!")
    conn.close()

except Exception as e:
    print(e)