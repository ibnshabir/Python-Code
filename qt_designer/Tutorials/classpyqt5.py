#from PyQt5.QtSerialPort import QSerialPort

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):    #inheriting all properties from AMainWindow, and will make modifications
    def __init__(self):         #method constructor calls in python
        super(MyWindow, self). __init__()   #calling parent constructor, parent class is QMainWindow
        self.setGeometry(200, 200, 300, 300)  # win.setGeometry(xpostion, yposition, width, height)
        self.setWindowTitle("Practicing pyqt5")  # the title taht appears on the top bar
        self.initUI()

    def initUI(self):   #some people omit this, i'll do it since following tutorial inside this we will place all the stuff we need in our window
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label")
        self.label.move(100, 0)

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("Click me")
        self.button1.move(100, 200)
        self.button1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()

#funcion to map the button to an event
def clicked():
    print("i was clicked")

def a_window():
    application = QApplication(sys.argv)    #giving config setup
    window = MyWindow()
    window.show()  #to show the window
    sys.exit(application.exec_()) #this makes sure the window shows up nicely and that there is a clean exit

a_window()