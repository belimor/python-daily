#!/usr/bin/python3

# datetime module is used for working with dates and times.

###################################
# Importing the datetime Module
from datetime import datetime

###################################
# Getting the Current Date and Time

# Current date and time
now = datetime.now()
print("Current date and time:", now)

# Current date only
today = now.date()
print("Todaye's date:", today)

# Current time only
current_time = now.time()
print("Current time:", current_time)

###################################
# Formatting Dates and Times

# Format the current date and time
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted)

# Custom formats
print("Day:", now.strftime("%A"))
print("Month:", now.strftime("%B"))
print("12-hour time:", now.strftime("%I:%M %p"))

###################################
# Parsing Strings to Dates

date_string = "2025-02-09 14:30:00 -0700"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S %z")
print("Parsed datetime:", parsed_date)

# # Time difference
time_difference = future_date - now
print("Time difference in days:", time_difference.days)




