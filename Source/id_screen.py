import sys

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow

from capture_image import capture_image


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(548, 328)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-40, -50, 661, 391))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(250, 40, 101, 61))
        self.label.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 130, 191, 51))
        self.lineEdit.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(210, 230, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {    background-color: rgb(75, 57, 239);\n"
"    color: white;\n"
"    border: none;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    font-size: 16px;\n"
"    cursor: pointer;\n"
" }\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(57, 210, 192);\n"
"}\n"
"\n"
"")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 548, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton.clicked.connect(self.Capture_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Student ID"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "       Enter Student ID"))
        self.pushButton.setText(_translate("MainWindow", "Capture"))

    def Capture_2(self):
        text1 = self.lineEdit.text()
        capture_image(0, text1)
