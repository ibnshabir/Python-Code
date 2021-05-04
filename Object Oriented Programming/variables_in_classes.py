#  instance variable and class (static) variables
#  namespace-> an area where you create and store object/ variables
    #class namespace-> where we store all class variables
    # object/ instance namespace-> where we store all instance variables

class Car:

    #  class (static) variable are declared outside the init method (constructor)
    wheels = 4

    def __init__(self):
        self.mil = 0
        self.comp = "Company"


corolla = Car()
civic = Car()


Car.wheels = 3  # class variable changing

corolla.mil = 30000
corolla.comp = "Toyota"

print(corolla.mil, corolla.comp, corolla.wheels)
print(civic.mil, civic.comp, Car.wheels)