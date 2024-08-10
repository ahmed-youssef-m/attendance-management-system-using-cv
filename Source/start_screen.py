import os

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1514, 752)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_14 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_14.setGeometry(QtCore.QRect(970, 660, 601, 80))
        self.widget_14.setObjectName("widget_14")
        self.label_8 = QtWidgets.QLabel(parent=self.widget_14)
        self.label_8.setGeometry(QtCore.QRect(310, 60, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(170, 0, 0);\n"
                                   "color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.widget_13 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_13.setGeometry(QtCore.QRect(220, 660, 601, 80))
        self.widget_13.setObjectName("widget_13")
        self.label_7 = QtWidgets.QLabel(parent=self.widget_13)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 401, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 221, 781))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.widget_5 = QtWidgets.QWidget(parent=self.widget)
        self.widget_5.setGeometry(QtCore.QRect(40, 59, 91, 61))
        self.widget_5.setStyleSheet("QWidget {\n"
                                    "    border: 5px solid rgb(75, 57, 239);\n"
                                    "    border-radius: 0 0 0 10px;\n"
                                    "}")
        self.widget_5.setObjectName("widget_5")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font-weight: bold;\n"
                                   "border:0px;")
        self.label_5.setObjectName("label_5")
        self.widget_6 = QtWidgets.QWidget(parent=self.widget)
        self.widget_6.setGeometry(QtCore.QRect(90, 90, 91, 61))
        self.widget_6.setStyleSheet("QWidget {\n"
                                    "    background-color: rgb(0, 0, 0);\n"
                                    "    border: 5px solid  rgb(57, 210, 192);\n"
                                    "    border-radius: 0 0 0 10px;\n"
                                    "}\n"
                                    "")
        self.widget_6.setObjectName("widget_6")
        self.label_6 = QtWidgets.QLabel(parent=self.widget_6)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "font-weight: bold;\n"
                                   "border:0px;")
        self.label_6.setObjectName("label_6")
        self.start = QtWidgets.QPushButton(parent=self.widget)
        self.start.setEnabled(True)
        self.start.setGeometry(QtCore.QRect(40, 370, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.start.setFont(font)
        self.start.setStyleSheet("QPushButton {  \n"
                                 " background-color:rgb(57, 210, 192);\n"
                                 "    color: white;\n"
                                 "    text-align: center;\n"
                                 "    font-size: 18px;\n"
                                 "    font-weight: bold;\n"
                                 "    cursor: pointer;\n"
                                 "  border-radius: 15px ;\n"
                                 " }\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: rgb(75, 57, 239);\n"
                                 "}\n"
                                 "QPushButton:clicked {\n"
                                 "    background-color: rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "")
        self.start.setFlat(True)
        self.start.setObjectName("start")
        self.view = QtWidgets.QPushButton(parent=self.widget)
        self.view.setEnabled(True)
        self.view.setGeometry(QtCore.QRect(40, 430, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.view.setFont(font)
        self.view.setStyleSheet("QPushButton {  \n"
                                " background-color:rgb(57, 210, 192);\n"
                                "    color: white;\n"
                                "    text-align: center;\n"
                                "    font-size: 18px;\n"
                                "    font-weight: bold;\n"
                                "    cursor: pointer;\n"
                                "  border-radius: 15px ;\n"
                                " }\n"
                                "QPushButton:hover {\n"
                                "    background-color: rgb(75, 57, 239);\n"
                                "}\n"
                                "QPushButton:clicked {\n"
                                "    background-color: rgb(255, 255, 255);\n"
                                "}\n"
                                "\n"
                                "")
        self.view.setFlat(True)
        self.view.setObjectName("view")
        self.widget_3 = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(220, -10, 1301, 431))
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 80px;\n"
                                    "margin-bottom:0px;")
        self.widget_3.setObjectName("widget_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(570, 90, 331, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 800 13pt \"MS Shell Dlg 2\";\n"
                                   " font-weight: bold;\n"
                                   "color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_2.setGeometry(QtCore.QRect(430, 79, 121, 71))
        self.widget_2.setStyleSheet("QWidget {\n"
                                    "    border: 5px solid rgb(75, 57, 239);\n"
                                    "    border-radius: 0 0 0 10px;\n"
                                    "}")
        self.widget_2.setObjectName("widget_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(0, 20, 41, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border:1px ;\n"
                                   "color: rgb(0, 0, 0);\n"
                                   "font-weight: bold;\n"
                                   "font: 650 italic 12pt \"MS Shell Dlg 2\";")
        self.label_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_9.setGeometry(QtCore.QRect(40, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border:1px ;\n"
                                   "color: rgb(0, 0, 0);\n"
                                   "font-weight: bold;\n"
                                   "font: 650 italic 12pt \"MS Shell Dlg 2\";")
        self.label_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.label_9.setObjectName("label_9")
        self.capture = QtWidgets.QPushButton(parent=self.centralwidget)
        self.capture.setEnabled(True)
        self.capture.setGeometry(QtCore.QRect(530, 530, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.capture.setFont(font)
        self.capture.setStyleSheet("QPushButton {    background-color: rgb(75, 57, 239);\n"
                                   "    color: white;\n"
                                   "    border: none;\n"
                                   "    text-align: center;\n"
                                   "    text-decoration: none;\n"
                                   "    font-size: 16px;\n"
                                   "    cursor: pointer;\n"
                                   " }\n"
                                   "QPushButton:hover {\n"
                                   "    background-color: rgb(57, 210, 192);\n"
                                   "}\n"
                                   "\n"
                                   "")
        self.capture.setFlat(False)
        self.capture.setObjectName("capture")
        self.train = QtWidgets.QPushButton(parent=self.centralwidget)
        self.train.setEnabled(True)
        self.train.setGeometry(QtCore.QRect(940, 530, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.train.setFont(font)
        self.train.setStyleSheet("QPushButton {    background-color: rgb(75, 57, 239);\n"
                                 "    color: white;\n"
                                 "    border: none;\n"
                                 "    text-align: center;\n"
                                 "    text-decoration: none;\n"
                                 "    font-size: 16px;\n"
                                 "    cursor: pointer;\n"
                                 " }\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: rgb(57, 210, 192);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "")
        self.train.setFlat(False)
        self.train.setObjectName("train")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1514, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.start.clicked.connect(self.Start)
        self.view.clicked.connect(self.View)
        self.capture.clicked.connect(self.Capture)
        self.train.clicked.connect(self.Train)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "Designed by The Project Team. v1.0.0"))
        self.label_7.setText(_translate("MainWindow", " © 2023-2024 The Project Team. All rights reserved."))
        self.label_5.setText(_translate("MainWindow", "CV-"))
        self.label_6.setText(_translate("MainWindow", " AMS"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.view.setText(_translate("MainWindow", "View"))
        self.label_4.setText(_translate("MainWindow", "Attendance Management system"))
        self.label_3.setText(_translate("MainWindow", "CV-"))
        self.label_9.setText(_translate("MainWindow", "AMS"))
        self.capture.setText(_translate("MainWindow", "Capture"))
        self.train.setText(_translate("MainWindow", "Train"))

    def Start(self):
        other_file_path = "recognizer.py"
        os.system(f"python {other_file_path}")


    def View(self):
        other_file_path = "open_excel.py"
        os.system(f"python {other_file_path}")

    def Capture(self):
        other_file_path = "id_start.py"
        os.system(f"python {other_file_path}")

    def Train(self):
        other_file_path = "faces_train.py"
        os.system(f"python {other_file_path}")
