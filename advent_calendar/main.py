#Advent Calendar

import random
import os
import sys
from datetime import date
from time import localtime

#open file to save information in
if os.path.exists("advent_save.txt"):
	save_file = open("advent_save.txt", "a")
else:
	save_file = open("advent_save.txt", "a")

#change where prints direct to
sys.stdout = save_file

rewards = ["A Christmas Dinner!",
			"Presents!",
			"Chocolate!",
			"Oranges"
]

#not very efficient, but readable
today_tuple = localtime()
today_year = today_tuple[0]
today_month = today_tuple[1]
today_day = today_tuple[2]
today = date(today_year, today_month, today_day).isoformat()

print(today)
print("Your reward is: ")
print(random.choice(rewards))
print("\n")
