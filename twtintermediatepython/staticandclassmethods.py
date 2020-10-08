# Static And Class Methods

# Static And Class Methods Are Decorators That Let Python Know That You Are Trying To Reference And Use Variables That Have Been Defined At The Class Level

class person(object):

    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, ' is ', self.age, ' years old')

newPerson = person('Aditya', 14)

print(person.getPopulation())
print(person.isAdult(91))