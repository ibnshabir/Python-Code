# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'threads.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 511, 171))
        self.groupBox.setObjectName("groupBox")

        self.progressBar_3 = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar_3.setGeometry(QtCore.QRect(320, 120, 118, 23))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 80, 101, 21))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 80, 91, 23))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(200, 120, 91, 23))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 120, 101, 21))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(40, 40, 101, 21))
        self.pushButton.setObjectName("pushButton")

        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setGeometry(QtCore.QRect(320, 40, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.progressBar_2 = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar_2.setGeometry(QtCore.QRect(320, 80, 118, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")

        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 40, 91, 23))
        self.pushButton_4.setObjectName("pushButton_4")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Testing Threads"))
        self.pushButton_2.setText(_translate("MainWindow", "Start Thread 2"))
        self.pushButton_5.setText(_translate("MainWindow", "stop thread 2"))
        self.pushButton_6.setText(_translate("MainWindow", "stop thread 3"))
        self.pushButton_3.setText(_translate("MainWindow", "Start Thread 3"))
        self.pushButton.setText(_translate("MainWindow", "Start Thread 1"))
        self.pushButton_4.setText(_translate("MainWindow", "Stop Thread 1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

