from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton,\
    QLabel, QGroupBox, QHBoxLayout
from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtCore import pyqtSlot
import sys
from opening_new_window_class import NewWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.num_click = 1
        self.nw = None

        self.setWindowTitle('my app')
        self.setGeometry(500,200,300,200)
        self.createLayout()
        self.show()

    def createLayout(self):
        self.gbox = QGroupBox('group box')
        hbox = QHBoxLayout(self)
        b1 = QPushButton('press me', self)
        b1.setGeometry(100, 10, 70, 30)
        b2 = QPushButton('press me', self)
        b2.setGeometry(100, 80, 70, 30)
        b3 = QPushButton("don't press", self)
        b3.setGeometry(100, 150, 70, 30)
        hbox.addWidget(b1)
        hbox.addWidget(b2)
        hbox.addWidget(b3)

        l1 = QLabel(self)
        l1.setText("I'm a label")
        l1.setGeometry(200, 100, 80, 30)
        hbox.addWidget(l1)

        b1.clicked.connect(self.b1_slot)
        b2.clicked.connect(self.b2_slot)
        b3.clicked.connect(self.b3_slot)

    @pyqtSlot()
    def b1_slot(self):
        print('good')
        port = QSerialPort()

    def b2_slot(self):
        print('ok')
        self.nw = NewWindow()

    def b3_slot(self):
        if self.num_click == 1:
            print('first warning')
        elif self.num_click == 2:
            print('second warning')
        else:
            print('you were warned')
            sys.exit()
        self.num_click += 1


if __name__ == "__main__":
    app = QApplication([])
    mw = MyWindow()
    sys.exit(app.exec())
