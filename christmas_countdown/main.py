#Christmas Countdown

from time import localtime
from datetime import date
import colorama
colorama.init()

if (localtime()[2] < 25 and #if it's before the 25th
	localtime()[1] == 12):
		christmas = date(localtime()[0], 12, 25) #makes christmas the 25th of December this year
else: #if it is after christmas this year
	christmas = date(localtime()[0]+1, 12, 25)
today = date(localtime()[0], localtime()[1], localtime()[2]) #localtime() returns a tuple in the format (year, month, day)

difference = christmas - today
difference = int(str(difference)[:3].rstrip()) #difference is the first three characters without spaces or newlines to the right
if localtime()[1] != 12: #if it's not December
	print(colorama.Fore.RED + str(difference) + " days until Christmas!")
else:
	print(colorama.Fore.GREEN + str(difference) + " days until Christmas!")
