class A:
    def feature_1(self):
        print('Feature 1 From A')
    def feature_2(self):
        print('Feature 2 From A')

class B:
    def feature_1(self):
        print('Feature 1 From B')

class C(B,A):
    def feature_3(self):
        print('Feature 3 From C')
    

c_object = C()
c_object.feature_1()

a = 13
b = 2
c = 14

print(int.__add__(a, b))

class Student:
    def __init__(self, marks, name):
        self.marks = marks
        self.name = name
    
    def __add__(self, other):
        m = self.marks + other.marks
        return m
    
    def __str__(self):
        return self.name + ' ' + str(self.marks)

    def __gt__(self, other):
        if self.marks > other.marks:
            return True
        else:
            return False

    def display_marks(self, bonus1: str):
        print(self.name, bonus1)

    def display_marks(self, bonus_marks):
        total = self.marks + bonus_marks
        print(self.name, total)


aditya = Student(99, 'Aditya')
shreyas = Student(60, 'Shreyas')

# print(aditya + shreyas)
# print(aditya)
# print(aditya > shreyas)

# num1 = 1
# num2 = 2
# print(num1 + num2)

aditya.display_marks(10)
shreyas.display_marks('10')