from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon
import sys

class MyWindow(QMainWindow): #inheritance-> using QMainWindow as the parent class for our MyWindow class
    def __init__(self):
        super().__init__()  #In python, will only call the derived class constructor
                                # therefore, used this special method to call the parent constructor as well

        #since creating a window, need the following

        #1. title
        #2. geometry-> location, size etc

        #data members
        self.title = "PyQt5 Window" #self is same as *this in C++

        self.xPosition = 100    #position in x-coordinate
        self.yPosition = 100    #position in y-coordinate
        self.width = 400        #width of the window
        self.height = 300       #height of the window


    #need to call the method in our window class, else the window will not appear
        self.setWindow()

   #create a method to set the properties
    def setWindow(self):    #have to pass self in parameter in order for it to make changes to the object working on

        # methods in class QMainWindow
        self.setWindowTitle(self.title)  # sets the title
        self.setGeometry(self.xPosition, self.yPosition, self.width, self.height)  # setting  the geometry of window

        #calling this method to set a home icon
        self.setWindowIcon(QIcon("homeIcon.png"))


        self.show()  #shows all the widgets



#this step is important
#it's like the main of the program
app = QApplication(sys.argv)    #creating an object for the class QApplication
                                #argv is the list of commandline arguments passed to the Python program.
                                #argv represents all the items that come along via the command line input,
                                #it's basically an array holding the command line arguments of our program.

                                #the order of creting these objects matters

window = MyWindow()     #creating an object for class MyWindow

sys.exit(app.exec())    #this is like the system("pause") in visual studio??? maybe something like it