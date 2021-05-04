class A:
    def __init__(self):
        self.height = 6

    def add_name(self, name):
        self.name = name

    def add_age(self, age):
        self.age = age

    def print_info(self):
        print(self.name, self.age)


a = A()
a.add_name('ali')
a.add_age(30)
a.print_info()
print(a.height)
