
class Computer:
    def config(self):
        print("i5, 16gb, 1TB")


comp1 = Computer()

#  2 ways of calling method
Computer.config(comp1)
comp1.config()  # def config(self): the object comp1 passed as parameter

print(type(comp1))
