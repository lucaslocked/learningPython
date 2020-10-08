# Instance Attributes
class ShippingContainer:
    # Class Attributes
        # Associated With The Class, But Not With Every Instance Of The Class
        # Basically An Attribute That Is Shared With All Instances Of The Class

    next_serial = 1337

    # Owner Code and Contents Are The Instance Attributes
    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = self.next_serial
        self.next_serial += 1

c1 = ShippingContainer("YML", ['books'])
print(c1.owner_code)
print(c1.contents)
print(c1.serial)

c2 = ShippingContainer("MAE", ['clothes'])
print(c2.owner_code)
print(c2.contents)
print(c2.serial)

c3 = ShippingContainer('AAA', ['tools'])
print(c3.owner_code)
print(c3.serial)
print(c3.contents)

# Scopes In Python
    # Local - Inside The Current Function
    # Enclosing - Inside The Enclosing Functions
    # Global - At The Top Level Of The Module
    # Built-In - In The Special Builtins Module
    # LEGB