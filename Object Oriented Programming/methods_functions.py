#  method-> calling on object itself
#  function-> will take an object, and apply an operation to it


x = 5
y = "hello"


def func(val):
    return val+1


print(func(x))      # function-> will take an object, and apply an operation to it
print(y.upper())    # method-> calling on object itself
