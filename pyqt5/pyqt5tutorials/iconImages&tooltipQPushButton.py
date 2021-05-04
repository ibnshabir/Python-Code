#was unable to display the icon insde the button
#was able top have the hover message on the button though


from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect, QSize
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #initializing data members in constructor
        title = "PyQt5 Window"
        xPos = 1000
        yPos = 500
        width = 300
        height = 250
        iconImg = "homeIcon.png"

        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(iconImg))
        self.setGeometry(xPos, yPos, width, height)

        self.forButton()

        self.show()

    #method for creating a push button
    def forButton(self):
        button = QPushButton("Click me", self)  #creating obj of QPushButton class
                                                #need to pass these parameters in
        #to move the button
        #button.move(50,50)
        #set geometry for button -> need to import QRect from QCore for this
        button.setGeometry(QRect(100,100,70,20))    #method in class QRect in module QCore
        button.setIcon(QIcon("homeIcon.png"))      #sets icon inside button
        button.setIconSize(QSize(20,20))    #sets size of the icon in button
                                                    #need to import the QCore class for this
        button.setToolTip("<h3>This is a click me button<h3>")  #upon hovering over the button, will display this messsage
                                                                #note: can use html isnide python! ex: he used a <h2> tag to make the msg bolder


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
