from PyQt5.QtWidgets import QMainWindow


class NewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "new window" #self is same as *this in C++

        self.xPosition = 100    #position in x-coordinate
        self.yPosition = 100    #position in y-coordinate
        self.width = 300        #width of the window
        self.height = 100       #height of the window

        self.setWindow()

    def setWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.xPosition, self.yPosition, self.width, self.height)

        self.show()
