# Static Methods
class ShippingContainer:

    next_serial = 1337

    # Static Method Used So That The Method Is Associated With The Class, Not With Each Instance
    @staticmethod
    def generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer.generate_serial()

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
