#  variables to store data and methods for behaviours
#  types of methods
#  1. instance methods   2. class methods   3. static methods

# Types of instance methods
# 1. accessors (getters)  2. mutators (setters)

#  Static method-> a method which has nothing to do with instance or class variable


class Student:
    school = "Concordia"  # class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    #  avg is an instance method, because passing self as parameter,
    #  which means it belongs to a particular object
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    #  note: function names should be lowercase
    def get_m1(self):
        return self.m1

    #  similar to C++, can either set variable's values in constructor or set methods
    def set_m1(self, value):
        self.m1 = value

    #  calling on class method giving error, therefore need to use decorator @
    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():  # when using static method, don't pass either self or cls in it
        print("this is Student class in abc module")


s1 = Student(90, 85, 76)
s2 = Student(79, 82, 87)

print(s1.avg())
print(Student.avg(s2))  # both ways are valid of calling methods
print(s1.get_m1())
s2.set_m1(85)
print(s2.get_m1())
print(Student.getSchool())
Student.info()
