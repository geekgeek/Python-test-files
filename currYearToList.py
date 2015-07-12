# Add current year to list
from datetime import date
yearToday= date.today().year

tu = [12,45]

tu.append(yearToday)

print(tu)

#Output:
# [12, 45, 2015]
