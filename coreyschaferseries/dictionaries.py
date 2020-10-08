student = {
    'name': "Aditya",
    'age': 14,
    'courses': ['Math', 'CompSci']
}
print(student)
#get specific assignment in dictionary
print(student['name'])

#add more assignments
student['phone_number'] = '555-5555'

#change assignments
student.update({
    'name': 'Shreyas',
    'age': 8,
    'courses': ['English', 'Art'],
    'phone': '123-4444'
})

print(student.values())
print(student.items())

for key in student:
    print(key)

for key in student.items():
    print(key)

for key, value in student.items():
    print(key,value)


if (1 < 12):
    print("True")