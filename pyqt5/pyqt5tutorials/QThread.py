from PyQt5.QtWidgets import QDialog, QApplication, QProgressBar, QVBoxLayout, QPushButton
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time
import sys


class MyThread(QThread):

    change_value = pyqtSignal(int)

    def run(self):
        cnt = 0
        while cnt < 100:
            cnt += 10

            time.sleep(0.5)
            self.change_value.emit(cnt)


class MyWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Window"
        self.x = 100
        self.y = 100
        self.w = 400
        self.h = 300
        self.setGeometry(self.x, self.y, self.w, self.h)
        self.setWindowTitle('Threads')

        self.setUI()

        self.show()

    def setUI(self):
        vbox = QVBoxLayout()
        self.pb1 = QProgressBar()
        self.pb1.setMaximum(100)
        vbox.addWidget(self.pb1)

        self.button = QPushButton('run progress bar')
        self.button.adjustSize()
        self.button.clicked.connect(self.startProgBar)
        vbox.addWidget(self.button)
        self.setLayout(vbox)


    def startProgBar(self):
        self.thread = MyThread()
        self.thread.change_value.connect(self.setProgressVal)
        self.thread.start()

    def setProgressVal (self, val):
        self.pb1.setValue(val)


app = QApplication(sys.argv)
window = MyWindow()
sys.exit(app.exec())
