class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info_a(self):
        print(self.name, self.age)


class B(A):
    def __init__(self, name, age, height):
        super().__init__(name, age)
        self.height = height

    def info_b(self):
        print(self.height)


b = B('ali', 32, '175')
b.info_a()
b.info_b()