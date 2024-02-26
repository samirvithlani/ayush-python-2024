#date...
from datetime import date

today = date.today()
print("Today's date:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
print("Weekday:", today.weekday())


StrDate = today.strftime("%d/%m/%y")
print("Date in dd/mm/yyyy format:", StrDate)