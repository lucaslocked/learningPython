first_name = 'Aditya'
last_name = 'Rawat'

sentence  = 'My name is {} {}.'.format(first_name, last_name)

sentence = f'My name is {first_name.upper()} {last_name.upper()}'

person = {
    'name': 'Aditya',
    'age': 14
}
sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])

sentence = f"My name is {person['name']} and I am {person['age']} years old"

calculation = f'4 times 11 is equal to {4 * 11}'

for n in range(1, 11):
    sentence = f'The current value is {n:02}'
    # print(sentence)

pi = 3.14159265

sentence = f'Pi is equal to {pi:.4f}'
#print(sentence)

from datetime import datetime

birthday = datetime(2020, 8, 30)

sentence = f'Aditya Rawat has a birthday party on {birthday:%B %d, %Y}'
print(sentence)