import datetime

start = int(raw_input("Enter start date (year, month, day):"))

end = int(raw_input("Enter end date (year, month, day):"))


days = datetime.datetime(start) - datetime.datetime(end)

print(days)  