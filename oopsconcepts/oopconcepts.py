# Python Object-Oriented Programming
# Part 1: Classes & Instances
# Part 2: Class Variables & Instance Variables
# Part 3: Methods, Class Methods, & Static Methods
# Part 4: Inheritance - Creating Subclasses
# Part 5: Special (Magic / Dunder) Methods
import datetime

# Class
class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
# Employee Instance/Objects
emp_1 = Employee('Aditya', 'Rawat', 50000)
emp_2 = Employee('Test', 'User', 45000)

# print(emp_1.fullname())
# Instance Variables (Slower)
# emp_1 = Employee('Aditya', 'Rawat', 50000)
# emp_1.first = 'Aditya'
# emp_1.last = 'Rawat'
# emp_1.email = 'Aditya.Rawat@company.com'
# emp_1.pay = 50000

# emp_1 = Employee('First', 'Last', 45000)
# emp_2.first = 'First'
# emp_2.last = 'Last'
# emp_2.email = 'First.Last@company.com'
# emp_2.pay = 45000

# Show that the fullname method works
# emp_1.fullname()
# print(Employee.fullname(emp_1))

#Raise The Salary Of Employees
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# Printing the emp_1 object as a dictionary (Will not show raise_amount)
# print(emp_1.__dict__)

# Printing the Employee Class as a dictionary (Will show raise_amount)
# print(Employee.__dict__)

# Showing raise_amount value in Class and objects
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# Raising The Value Of raise_amount
# Employee.raise_amount = 1.05 <--- Changes raise_amount for class and all instances
# emp_1.raise_amount = 1.05 <--- Changes raise_amount only for that instance (Similar for emp_2 as well)

# Shows the number of employees, but really just is the number of instances created
# print(Employee.num_of_emps)

# Creating Objects From Strings
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-80000'
# emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split('-')

# new_emp_1 = Employee(first, last, pay)
# print(new_emp_1.email)

# Checking if the given date is a workday or not
# my_date = datetime.date(2017, 7, 10)
# print(Employee.is_workday(my_date))

