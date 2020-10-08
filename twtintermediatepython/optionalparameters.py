# Optional Parameters Tutorial #1

# Optional Parameters Are Parameters That Can Be Referenced Optionally In An Instance Of A Class. But This Will Only Work If You Set A Default Value For That Instance Variable

class car(object):
    def __init__(self, make, model, year, condition='New', kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms
    
    def display(self, showAll=True):
        if showAll:
            print("This Car Is A '{}' '{}' From '{}'. It Is '{}' And Has '{}' KMs".format(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This Car Is A '{}' '{}' From '{}'".format(self.make, self.model, self.year))
whip = car('Ford', 'Fusion', 2012, 'New', 0)

default_whip = car('Ford', 'Fusion', 2020)