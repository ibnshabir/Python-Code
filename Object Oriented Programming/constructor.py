#  size of object dependant on number of variables and size of each variable
#  who allocates the size?  -> the constructor

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


p1 = Person("Eesa", 1)
p2 = Person("Hafsa", 1.2)

if p1.compare(p2):
    print("They are the same age")
else:
    print("They have different ages")