from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QSlider, QVBoxLayout


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()

        self.init_ui()

    def init_ui(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout(self)
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)

        sld.valueChanged.connect(lcd.display)

        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle("s n s")

        self.show()


def run():
    app = QApplication([])
    mw = MyWidget()
    app.exec_() #When we call the application's exec_() method,
                # the application enters the main loop.
                #The main loop fetches events and sends them to the objects.


if __name__ == "__main__":
    run()
