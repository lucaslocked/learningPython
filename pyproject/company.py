class Address:
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
    
    def get_address(self):
        return self.street + ' ' + self.city + ', ' + self.state + ' ' + str(self.zip)

class Company:
    def __init__(self, co_name, co_address: Address, employees):
        self.co_name = co_name
        self.co_address = co_address
        self.employees = employees

class Employee:
    def __init__(self, first_name, last_name, age, address: Address, company: Company, role, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.company = company
        self.role = role
        self.salary = salary

    def get_company_name(self):
        return self.company.co_name
    
    def fullname(self):
        return self.first_name + ' ' + self.last_name


# Company Objects
balboa = Company('Balboa', Address('575 Anton Blvd', 'Costa Mesa', 'California', 92626), 23)
rgp = Company('RGP', Address('17101 Armstrong Ave', 'Irvine', 'California', 92614), 12)

# Employee Objects
emp_1 = Employee('Aditya', 'Rawat', 14, Address('65 Darby', 'Irvine', 'California', 92620), balboa, 'Programmer', 50000)
emp_2 = Employee('Shreyas', 'Rawat', 8, Address('65 Darby', 'Irvine', 'California', 92620), rgp, 'Programmer', 100000)

print('Name: ' + emp_1.fullname())
print('Age: ' + str(emp_1.age))
print('Address: ' + emp_1.address.get_address())
print('Works At: ' + emp_1.company.co_name)
print('Work Address: ' + emp_1.company.co_address.get_address())
print('# Of Colleagues: ' + str(emp_1.company.employees))
print('Role: ' + emp_1.role)
print('Earns: $' + str(emp_1.salary))
print('--------------------------------------------------------')
print('Name: ' + emp_2.fullname())
print('Age: ' + str(emp_2.age))
print('Address: ' + emp_2.address.get_address())
print('Works At: ' + emp_2.company.co_name)
print('Work Address: ' + emp_2.company.co_address.get_address())
print('# Of Colleagues: ' + str(emp_2.company.employees))
print('Role: ' + emp_2.role)
print('Earns: $' + str(emp_2.salary))