# Event:
# user action ->clicking button, selecting item
# when  an event takes place, each PyQt5 widget can emit a signal
# Signal:
# signal doesn't execute any action
# ex: clicking of the button is a signal
# a signal doesn't execute any action, action performed by slot
# Slot:
# ex: upon the click of a button, do certain action,
# i.e: close the window, print something etc


from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect, QSize
import sys


class MyWindow(QMainWindow):  # inheritance
    def __init__(self):
        super().__init__()

        # data members
        self.title = "PyQt5 Events and Signals"  # self is same as *this in C++

        self.xPosition = 1000  # position in x-coordinate
        self.yPosition = 500  # position in y-coordinate
        self.width = 400  # width of the window
        self.height = 300  # height of the window

        # need to call the method in our window class, else the window will not appear
        self.setWindow()

    # create a method to set the properties
    def setWindow(self):
        # methods in class QMainWindow
        self.setWindowTitle(self.title)  # sets the title
        self.setGeometry(self.xPosition, self.yPosition, self.width, self.height)  # setting  the geometry of window

        # calling this method to set a home icon
        self.setWindowIcon(QIcon("homeIcon.png"))
        self.createButton()

        self.show()  # shows all the widgets

    # #method to send signal as message
    # def createButton(self):
    #     button = QPushButton("Click me", self)  # creating obj of QPushButton class
    #     button.setGeometry(QRect(100, 100, 70, 20))  # method in class QRect in module QCore
    #     button.setIcon(QIcon("homeIcon.png"))      #sets icon inside button
    #     button.setIconSize(QSize(20,20))    #sets size of the icon in button
    #
    #     #need to connect the slot with the pyqt5 clicked signal
    #     button.clicked.connect(self.ClickMe)    #want to connect the clicked signal with the ClickMe method

    # method to send signal to close the application
    def createButton(self):
        button = QPushButton("Close Application", self)  # creating obj of QPushButton class
        button.setGeometry(QRect(100, 100, 100, 50))  # method in class QRect in module QCore
        button.setIcon(QIcon("homeIcon.png"))  # sets icon inside button
        button.setIconSize(QSize(20, 20))  # sets size of the icon in button

        # need to connect the slot with the pyqt5 clicked signal
        button.clicked.connect(self.ClickMe)  # want to connect the clicked signal with the ClickMe method

    # # #method to send signal as message
    # def ClickMe(self):
    #     print("Hello World")
    # method to send signal to close the application
    def ClickMe(self):
        sys.exit()


app = QApplication(sys.argv)

window = MyWindow()   # creating an object for class MyWindow

sys.exit(app.exec())  # this is like the system("pause") in visual studio??? maybe something like it
