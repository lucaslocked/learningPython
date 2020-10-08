multi_line_str = '''
    Hello This is cool kid Aditya.
'''

# Arbitrary Arguments *args
# Used when you do not know how many arguements will be passed into your function
def my_function(*kids):
    print('The youngest child is ' + kids[2])
my_function("Emil", "Tobias", "Linus")


# Arbitrary Keyword Arguements **kwargs 
# Used when you do not know how many keyword arguments will be passed into your function
def name_that_child(**child):
    print('His name is: ' + child["fname"] + ' ' + child["lname"])

name_that_child(fname = 'Aditya', lname = 'Rawat')

#Default Parameter Value
def the_mother_land(country = 'India'):
    print('The Mother Land Is ' + country)

the_mother_land('United States')
the_mother_land()

pop_list_test = [1, 2, 3, 4, 5, 6]
pop_list_test.pop()
print(pop_list_test)
# If you use pop and don't pass anything, it will remove the last element in a list by default
# .upper() will capitalize entire string
# .capitalize() will capitalize the first character
# Neither capitalize specific characters or portions of string
upper_str = 'aditya'
print(upper_str.upper())
print(upper_str.capitalize())

# 'str' in str will return a boolean
check = 'adi' in upper_str
print(check)

who = 'Aditya'
what = 'super cool'
full_sentence = 'I am {} and I am {}'
format_full_sentence = full_sentence.format(who, what)
print(format_full_sentence)

print("Aditya is 'super' cool")


# TIME TO BE COOL AND USE ALL THE STRING METHODS
string_that_will_be_tested_brutally = "Hi There. It's your boy Aditya Rawat. Welcome back to my minecraft channel"
# Capitalize
print('.capitalize(): ' + string_that_will_be_tested_brutally.capitalize())
print('.casefold(): ' + string_that_will_be_tested_brutally.casefold())
print('.center(): ' + string_that_will_be_tested_brutally.center(100))
print('.count: ', end='')
print(string_that_will_be_tested_brutally.count("Aditya"))
print
