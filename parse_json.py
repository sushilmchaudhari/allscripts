import json
from time_calc import time_calc

with open('test1.json', 'r') as f:
    test_dict = json.load(f)

job_name = test_dict['jobName']

start_time = test_dict['results']['items'][0]['start_time']

length_of_items_array = len(test_dict['results']['items'])

print (job_name)
print (start_time)
print (length_of_items_array)

for item in test_dict['results']['items']:
    if 'start_time' in item:
        print "Start time is: ", item['start_time'], "\n"
        formatted_start_time = time_calc(item['start_time'])
        print "Formatted Start time is: ", formatted_start_time, "\n"
        
    if 'end_time' in item:
        print "End time is: ", item['end_time'], "\n"
        formatted_end_time = time_calc(item['end_time'])
        print "Formatted End time is: ", formatted_end_time, "\n"
