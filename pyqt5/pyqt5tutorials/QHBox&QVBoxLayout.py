#to control the UI components
    #to manage the layout
    #organizing widgets
#have different layouts in pyqt5
    #QHBoxLayout-> lines up widgets horizontally
    #QVBoxLayout-> organizes the widgets vertically
    #QGridLayout-> organizes the widgets in rows and coloumns




from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

import sys

class MyWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Events and Signals"  # self is same as *this in C++
        self.xPosition = 500  # position in x-coordinate
        self.yPosition = 200  # position in y-coordinate
        self.width = 400  # width of the window
        self.height = 400  # height of the window
        self.iconImg = "homeIcon.png"

        self.setWindow()


    def setWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.iconImg))
        self.setGeometry(self.xPosition, self.yPosition, self.width, self.height)

        self.createLayout()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def createLayout(self):
        self.groupBox = QGroupBox("What's your favorite sport")  # this is eliminating multiple steps
                                                                 # it's instantiating an object of class QGroupBox and initializing it
        hBoxlayout = QHBoxLayout()

        button1 = QPushButton("volleyball", self)
        button1.setGeometry(100,100,150,50)
        button1.setIcon(QIcon("homeIcon.png"))  # put diff icon here i.e: football etc
        button1.setIconSize(QSize(40,20))
        button1.setMinimumHeight(40)
        hBoxlayout.addWidget(button1)

        button2 = QPushButton("cricket", self)
        button2.setGeometry(100, 100, 150, 50)
        button2.setIcon(QIcon("homeIcon.png"))
        button2.setIconSize(QSize(40, 20))
        button2.setMinimumHeight(40)
        hBoxlayout.addWidget(button2)

        button3 = QPushButton("football", self)
        button3.setGeometry(100, 100, 150, 50)
        button3.setIcon(QIcon("homeIcon.png"))
        button3.setIconSize(QSize(40, 20))
        button3.setMinimumHeight(40)
        hBoxlayout.addWidget(button3)




        self.groupBox.setLayout(hBoxlayout)





if __name__ == "__main__":
    app = QApplication(sys.argv)    #why passing sys.argv??
                                    #check in creatingWindow.py
    window = MyWindow()
    sys.exit(app.exec())
