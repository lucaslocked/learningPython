# Lists
courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Physical Education', 'World Languages']
nums = [1, 3, 2, 4]

print(len(courses))
print(courses[1])
print(courses[-1]) # Negative Indexes Go Reverse Order
print(courses[0:2])
print(courses[2:]) # Index 2 To The End
print(courses[:2]) # Index 0 To Index Two

courses.append('Art') # Adds New Value To The End Of The List
courses.insert(0, 'English') # Adds New Value To Specifically Defined Index

# courses.append(courses_2) # Will Add, But With Extra Brackets
courses.extend(courses_2) # Will Add The Way We Want It

courses.remove('Math')

courses.pop() # Removes The Value At The Last Index

courses.reverse() # Will Reverse The Current Order Of The List
nums.reverse()
# courses.sort(reverse='True') # Another Way To Reverse The Order
nums.sort(reverse=True) #--^
print(courses)
courses.sort() # Sort by Alphabetical Order
nums.sort() # Sort By Numerical Order
sorted_courses = sorted(courses) # Another Function To Sort
sorted_nums = sorted(nums) # ----^

min(nums) # Return Smallest Number
max(nums) # Return Largest Number

# Will Go Through The List & Print Each Course
for course in courses:
    print(course)

# Will Go Through List & Print Course's Index & Course
for index, course in enumerate(courses):
    print(index, course)

# Will Go Through List & Print Course's Index Starting From 1 & Course
for index, course in enumerate(courses, start = 1):
    print(index, course)
