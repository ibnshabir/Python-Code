from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #initializing data members in constructor
        title = "PyQt5 Window"
        xPos = 200
        yPos = 100
        width = 300
        height = 250
        iconImg = "homeIcon.png"

        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(iconImg))
        self.setGeometry(xPos, yPos, width, height)

        self.forButton()    # need to put before self.show method

        self.show()

    #method for creating a push button
    def forButton(self):
        button = QPushButton("Click me", self)  #creating obj of QPushButton class
                                                #need to pass these parameters in
        #to move the button
        #button.move(50,50)
        #set geometry for button -> need to import QRect from QCore for this
        button.setGeometry(QRect(100,100,70,20))    #method in class QRect in module QCore


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
