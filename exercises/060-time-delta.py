#!/usr/bin/python3

# When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

# Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

# Day dd Mon yyyy hh:mm:ss +xxxx

# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

# Input Format

# The first line contains T, the number of testcases.
# Each testcase contains 2 lines, representing time t(1) and time t(2).

# Constraints
# - Input contains only valid timestamps
# - year <= 3000

# Output Format

# Print the absolute difference (t(1)-t(2)) in seconds.

# Sample Input 0

mline = """
# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000
# Sample Output 0
# 25200
# 88200
"""
print(mline)

# Explanation 0
# In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is 7x3600 seconds or 25200 seconds.
# Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or 24x3600 + 30x60 = 88200 

import math
import os
import random
import re
import sys
from datetime import datetime, timezone

#t1 = "Sat 02 May 2015 19:54:36 +0530"
#t2 = "Fri 01 May 2015 13:54:36 -0000"
t1 = "Sun 10 May 2015 13:54:36 -0700"
t2 = "Sun 10 May 2015 13:54:36 -0000"

parsed_date1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
parsed_date2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
print("Parsed datetime:", parsed_date1.astimezone(timezone.utc))
print("Parsed datetime:", parsed_date2.astimezone(timezone.utc))
t1_utc = parsed_date1.astimezone(timezone.utc)
t2_utc = parsed_date2.astimezone(timezone.utc)

#utc_date = parsed_date.astimezone(timezone.utc)
time_difference = t2_utc - t1_utc
print("Time difference in days:", round(abs(time_difference.total_seconds())))



# Complete the time_delta function below.
#def time_delta(t1, t2):
#    parsed_date1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
#    parsed_date2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
#    t1_utc = parsed_date1.astimezone(timezone.utc)
#    t2_utc = parsed_date2.astimezone(timezone.utc)
#    time_difference = t2_utc - t1_utc
#    return str(round(abs(time_difference.total_seconds())))
#
#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    t = int(input())
#    for t_itr in range(t):
#        t1 = input()
#        t2 = input()
#        delta = time_delta(t1, t2)
#        fptr.write(delta + '\n')
#    fptr.close()

