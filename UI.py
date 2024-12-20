# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConvertPlus.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 330)
        MainWindow.setMinimumSize(QtCore.QSize(400, 330))
        MainWindow.setMaximumSize(QtCore.QSize(400, 330))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #808080")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 100))
        self.frame.setStyleSheet("background-color: #C0C0C0")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ConvertPlus = QtWidgets.QLabel(self.frame)
        self.ConvertPlus.setGeometry(QtCore.QRect(0, 0, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Cooper Black")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.ConvertPlus.setFont(font)
        self.ConvertPlus.setStyleSheet("border: 2px solid #FFFFFF;\n"
"")
        self.ConvertPlus.setAlignment(QtCore.Qt.AlignCenter)
        self.ConvertPlus.setObjectName("ConvertPlus")
        self.Sum1 = QtWidgets.QLineEdit(self.centralwidget)
        self.Sum1.setGeometry(QtCore.QRect(40, 130, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Haettenschweiler")
        font.setPointSize(30)
        self.Sum1.setFont(font)
        self.Sum1.setStyleSheet("background-color: Silver;\n"
"color:white;\n"
"border-radius: 15;\n"
"border: 2px solid #FFFFFF;")
        self.Sum1.setText("")
        self.Sum1.setAlignment(QtCore.Qt.AlignCenter)
        self.Sum1.setObjectName("Sum1")
        self.Sum2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Sum2.setGeometry(QtCore.QRect(40, 250, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Haettenschweiler")
        font.setPointSize(30)
        self.Sum2.setFont(font)
        self.Sum2.setStyleSheet("background-color: Silver;\n"
"color:white;\n"
"border-radius: 15;\n"
"border: 2px solid #FFFFFF;")
        self.Sum2.setText("")
        self.Sum2.setAlignment(QtCore.Qt.AlignCenter)
        self.Sum2.setObjectName("Sum2")
        self.Sum1BOX = QtWidgets.QComboBox(self.centralwidget)
        self.Sum1BOX.setGeometry(QtCore.QRect(260, 135, 120, 40))
        self.Sum1BOX.setStyleSheet("background-color: Silver;\n"
"color:white;\n"
"border-radius: 5;\n"
"border: 2px solid #FFFFFF;")
        self.Sum1BOX.setObjectName("Sum1BOX")
        self.ButtonSWAP = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonSWAP.setGeometry(QtCore.QRect(120, 190, 50, 50))
        self.ButtonSWAP.setStyleSheet("background-color: Silver;\n"
"color:white;\n"
"border-radius: 16;\n"
"border: 2px solid #FFFFFF;")
        self.ButtonSWAP.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Pictures/Картинки/помойка/arrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ButtonSWAP.setIcon(icon)
        self.ButtonSWAP.setIconSize(QtCore.QSize(30, 30))
        self.ButtonSWAP.setObjectName("ButtonSWAP")
        self.Sum2BOX = QtWidgets.QComboBox(self.centralwidget)
        self.Sum2BOX.setGeometry(QtCore.QRect(260, 255, 120, 40))
        self.Sum2BOX.setStyleSheet("background-color: Silver;\n"
"color:white;\n"
"border-radius: 5;\n"
"border: 2px solid #FFFFFF;")
        self.Sum2BOX.setObjectName("Sum2BOX")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ConvertPlus.setText(_translate("MainWindow", "ConvertPlus"))