from datetime import datetime, timedelta, timezone


now = datetime.now()
print(now)


birthday = datetime(2005, 9, 20)
print(birthday)


print(now.strftime("%d/%m/%Y"))
print(now.strftime("%A"))


future = now + timedelta(days=7)

difference = future - now

print(difference.days)


utc_time = datetime.now(timezone.utc)

print(utc_time)
