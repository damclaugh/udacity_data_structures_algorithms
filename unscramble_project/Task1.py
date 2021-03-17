"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

texts_send = [item[0] for item in texts]
texts_rec = [item[1] for item in texts]
calls_send = [item[0] for item in calls]
calls_rec = [item[1] for item in calls]

unique_nums = len(set(texts_send + texts_rec + calls_send + calls_rec))

print("There are {} different telephone numbers in the records.".format(unique_nums))
