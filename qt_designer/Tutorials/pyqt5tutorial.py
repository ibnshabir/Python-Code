#from PyQt5.QtSerialPort import QSerialPort

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow   #can also use QWidget, similar to QMainWindow
import sys

#funcion to map the button to an event
def clicked():
    print("i was clicked")

#when working with appplication
    #step 1:  define an application
        #create function for this

def a_window():
    application = QApplication(sys.argv)    #giving config setup
                                    # knowing what os app running on, how to display the window etc,
                                    # getting app setup,

    window = QMainWindow()

    #step 2: size and title of my_window

    window.setGeometry(200, 200, 300, 300) #win.setGeometry(xpostion, yposition, width, height)


    # x and y positions are the coordinates, it is pixels, so if x and y = 0,
        # then widget will be at the top left corner
        #if we have x and y = 100, then it will move 100 pixcels to the right and bottom
    #the width and height parameters are to size the widget

    window.setWindowTitle("Practicing pyqt5")  #the title taht appears on the top bar

    #adding label to the window
    label = QtWidgets.QLabel(window)    #in parameters pass where do you want the label to be (in the window)
    label.setText("my first label")
    label.move(100,0)

    #adding button to the window
    button1 = QtWidgets.QPushButton(window)
    button1.setText("Click me")
    button1.move(100,200)
    button1.clicked.connect(clicked)

    #need to map the button to an event, some response when clicking it
    #need to define a function for that (on top function clicked)

    window.show()  #to show the window
    sys.exit(application.exec_()) #this makes sure the window shows up nicely and that there is a clean exit

a_window()

#This code was used for creating a label and button, but it doesn't modify or interact with the other components of the window
    #i.e: changing the label etc. therefore need to edit it, therefore will start a class in another file -->

