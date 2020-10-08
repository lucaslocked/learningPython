from my_modules import find_index, test_string
import sys
import math
import datetime
import calendar
import os

courses = ['History', 'Math', 'Physics', 'CompSci']

# # index = find_index(courses, 'Math')
# # print(index)
# # print(test_string)
# # print(sys.path)

# random_course = random.choice(courses)

# print(random_course)

rads = math.radians(90)

print(math.sin(rads))

today = datetime.date.today()
print(today)

print(calendar.isleap(2017))

print(os.getcwd())

print(os.__file__)