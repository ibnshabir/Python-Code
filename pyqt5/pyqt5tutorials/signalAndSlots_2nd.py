from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()     #method to initialize the ui

    def init_ui(self):
        self.setGeometry(100,100,300,300)
        self.setWindowTitle("Buttons and events")

    #adding a label
        self.label = QLabel(self)
        self.label.setText("Hello")
        self.label.move(10, 10)

    #add a button
        self.btn = QPushButton(self)
        self.btn.setText("Push here")
        self.btn.move(10, 50)

        #responding to the event
            #the signal is called clicked
            #we'll connect inside the slot method btn_clicked
        self.btn.clicked.connect(self.btn_clicked)

        self.show()


    def btn_clicked(self):
        self.label.setText("Thanks for pressing the button")
        self.label.adjustSize()


def run():
    app = QApplication([])    #setup a QApplication
                                #can pass sys.argv in here if import sys
                                    #will pass all the command line options that get passed in when application starts
    cw = CustomWidget()
    app.exec_()             #the executable
if __name__ == "__main__":
    run()