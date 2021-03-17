
from operator import itemgetter

"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
call_dict = {}
for item in calls:
    if item[0] not in call_dict: 
        call_dict[item[0]] = int(item[3])
    else:
        call_dict[item[0]] += int(item[3])
    if item[1] not in call_dict:
        call_dict[item[1]] = int(item[3])
    else:
        call_dict[item[1]] += int(item[3])

sorted_list = sorted(call_dict.items(), key = itemgetter(1), reverse = True)

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(sorted_list[0][0], sorted_list[0][1]))
