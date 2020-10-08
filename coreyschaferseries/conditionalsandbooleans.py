if False:
    print("The condition was true")

language = "Python"
if language == "Python":
    print("True")

#Comparisons in Python
    #Equal : ==
    #Not Equal : !=
    #Greater Than : >
    #Less Than : <
    #Greater or Equal : >=
    #Less or Equal : <=
    #Object Identity : is

language_1 = "Java"
if language_1 == "Python":
    print("True")
elif language == "Python":
    print("True")
else:
    print("False")

#and
#or
#not

user = "Admin"
logged_in = True

if user == 'Admin' and logged_in:
    print("You are now in the admin page")
else:
    print("Entered credentials are incorrect")

a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(id(a) == id(b))

#False values
#False
#None
#Zero of any numerical values
#Any empty sequence, '', (), []
#Any empty mapping {}