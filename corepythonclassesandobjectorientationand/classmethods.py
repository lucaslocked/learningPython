from . import iso6346

# Class Methods
class ShippingContainer:

    next_serial = 1337

    # Alternative to the @staticmethod. This way, the method becomes an attribute to the class, and is referenced later as such
    @classmethod
    # @staticmethod
    def generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    # Use The "Named Constructor" Idiom
    @classmethod
    # Creates An 'Empty Container'
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @staticmethod
    def make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code = owner_code,
            serial = str(serial).zfill(6)
        )

    @classmethod
    # Create A Container With Items
    def create_with_items(cls, owner_code, contents):
        return cls(self, owner_code, contents=list(items))

    


    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.generate_serial()
        self.bic = ShippingContainer.make_bic_code(
            owner_code = owner_code,
            serial = ShippingContainer.generate_serial()
        )

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
print(c3.bic)