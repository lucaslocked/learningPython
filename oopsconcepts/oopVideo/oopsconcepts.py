class ComputerConfig:
    def __init__(self, cpu, ram, g_card, ssd, hdd):
        self.cpu = cpu
        self.ram = ram
        self.g_card = g_card
        self.ssd = ssd
        self.hdd = hdd

class Computer:
    
    # def config(self) -> str:
    #     return "i7, 16gb, gtx1060, 128gb, 1TB"
    def __init__(self, config):
        self.config = config
        
   # def config(self) -> ComputerConfig:    
        #return self.config;
         

aditya_laptop = Computer(ComputerConfig("i7", '16gb', 'gtx1060', '128gb', '1TB'))
shreyas_laptop = Computer(ComputerConfig("i7", '16gb', 'gtx1060', '128gb', '1TB'))

config = aditya_laptop.config
print(config.cpu)

class Name:
    def __init__(self, first, middle, last):
        self.first = first
        self.middle = middle
        self.last = last
    
    def fullname(self):
        return self.first + ' ' + self.middle + ' ' + self.last

class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state
    
    def full_address(self):
        return self.street + ' ' + self.city + ', ' + self.state

class Person:
    def __init__(self, name: Name, address: Address):
        self.name = name
        self.address = address


aditya = Person(Name('Aditya', 'Middle', 'Rawat'), Address('65 Darby', 'Irvine', 'California'))

print(aditya.name.fullname())
print(aditya.address.full_address())
