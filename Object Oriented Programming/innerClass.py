#  the object of the inner class is created inside the def __int__ method of the outer class


class Student:
    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.lap = self.Laptop()  # lap is object of the inner class

    def show(self):
        print(self.name, self.num)
        print(self.lap.lapInfo())

    class Laptop:
        def __init__(self):
            self.brand = "Dell"
            self.cpu = "i5"
            self.ram = 8

        def lapInfo(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Ali', 123567)
s2 = Student('Eesa', 456890)



s1.show()
#s1.lap.lapInfo()  # obj_of_outer_class.obj_of_inner_class.method_of_inner_class
s2.show()

