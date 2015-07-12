# Add current year, month and day to list
from datetime import date

yearToday= date.today().year
month = date.today().month
day = date.today().isoweekday()


list1 = []

list1.append(yearToday)
list1.append(month)
list1.append(day)

print(list1)
