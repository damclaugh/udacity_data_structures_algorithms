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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# Part A
bang_calls = set()
for num in calls:
  if num[0].startswith('(080)'):
    bang_calls.add(num[1])

codes_list = set()
for num in bang_calls:
  if num.startswith('('):
    code = num[num.find('(')+1:num.find(')')]
    codes_list.add(code)
  elif num.startswith('140'):
    codes_list.add('140')
  elif num.startswith(('7', '8', '9')):
    codes_list.add(num[0:4])

sorted_list = sorted(codes_list)

print("The numbers called by people in Bangalore have codes: ")
print(*sorted_list, sep='\n')


# Part B
all_bang_calls = []
for num in calls:
  if num[0].startswith('(080)'):
    all_bang_calls.append(num[1])

code = '(080)'
fix_num = len([num for num in all_bang_calls if code in num])

percent = round((fix_num/len(all_bang_calls) * 100), 2)

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent))
