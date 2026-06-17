from datetime import datetime, timedelta, timezone

# Current date and time
now = datetime.now()
print(now)

# Create a date
birthday = datetime(2005, 9, 20)
print(birthday)

# Format date
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%A"))

# Time difference
future = now + timedelta(days=7)

difference = future - now

print(difference.days)

# Timezone example
utc_time = datetime.now(timezone.utc)

print(utc_time)