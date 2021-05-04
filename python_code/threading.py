#  to make a thread, need to make a function that acts like the thread
#  to turn function into a thread, need to make a thread
#  to make the thread, need to use the threading module
#  store the thread in a variable i.e: x
#  define target inside the Thread(target=func), which is the function we want to run
#  only put name of the function, no brackets
#  if want to pass arguments to your function, need to pass another parameter in the Thread(args=())
#  args = () takes a tuple value, so if hav ey as parameter in func, the n will pass a value in agrs = (4,)
#  need to add comma after the value so  it treats as a list, else will remove commas and treat as value
#  thread objects work a bit differently then regular Python objects
#  to run another thread, need to x.start
#  by default, the program will have one thread, called the main thread
#  by x.start(), starting a second thread
#  to see the number of threads, use print(threadObj.activeCount())
'''
from PyQt5.QtCore import QThread
import time


# need to make a function that acts like the thread
def func(self):
    print('ran')
    time.sleep(1)
    print('done')


t = QThread()
t.start()
func(t)
print("1")
'''

import threading
from time import sleep

def func():
    print('start')
    sleep(1)
    print('done')

t = threading.Thread()
t.start()
#print('1')