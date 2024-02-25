import random
from datetime import datetime

#year, month, date
year = input("Enter the year you were born (YYYY): ")
month = input("Enter the month you were born (MM): ")
day = input("Enter the day you were born (DD): ")

date_of_birth = year + month + day

#time thingy
'''
`datetime.now()` gets the current date and time, 
and `strftime("%H%M")` is used to format that time to show only the hour
and minute in a 24-hour format without any separators.
'''
current_time = datetime.now().strftime("%H%M")

input_data = date_of_birth + current_time

#random 4-digit code based on the combined data
random.seed(input_data)
random_code = random.randint(1000, 9999)

print("Generated 4-digit code:", random_code)
