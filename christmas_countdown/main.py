#Christmas Countdown

from time import localtime
from datetime import date

christmas = date(localtime()[0], 12, 25) #makes christmas the 25th of December this year
today = date(localtime()[0], 12, 26) #localtime() returns a tuple in the format (year, month, day)

difference = christmas - today
print(str(difference)[:-9] + " until Christmas!")
