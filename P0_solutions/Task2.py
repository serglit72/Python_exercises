"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('P0_solutions/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('P0_solutions/calls.csv', 'r') as f:
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
longest = {}

key = 0
value = 0

if len(calls) !=0:
   
    for row in calls:
        if row[0] not in longest.keys():
            longest[row[0]] = int(row[3])
        else:
            value = longest.get(row[0])
            value += int(row[3])
            longest[row[0]] = value

    for row in calls:
        if row[1] not in longest.keys():
            longest[row[1]] = int(row[3])
        else:
            value = longest.get(row[1])
            value += int(row[3])
            longest[row[1]] = value

max_duration = max(longest.values())
phone_number = ""
for key,value in longest.items():
    if max_duration == value:
        phone_number = key

        
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_number,max_duration))

