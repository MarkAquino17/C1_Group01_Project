# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginPage.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnLogin.setGeometry(QtCore.QRect(370, 330, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 180, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 230, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textUsername = QtWidgets.QTextEdit(self.centralwidget)
        self.textUsername.setGeometry(QtCore.QRect(330, 180, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textUsername.setFont(font)
        self.textUsername.setObjectName("textUsername")
        self.textPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.textPassword.setGeometry(QtCore.QRect(330, 240, 261, 41))
        self.textPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textPassword.setFont(font)
        self.textPassword.setObjectName("textEdit")
        self.btnBack = QtWidgets.QPushButton(self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(580, 330, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.btnBack.setText(_translate("MainWindow", "Back"))

