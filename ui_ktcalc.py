# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ktcalc.ui'
#
# Created: Thu Jul 25 07:10:39 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(291, 309)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inverseButton = QtGui.QPushButton(self.centralwidget)
        self.inverseButton.setGeometry(QtCore.QRect(227, 145, 55, 40))
        self.inverseButton.setObjectName("inverseButton")
        self.clearButton = QtGui.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(227, 184, 55, 40))
        self.clearButton.setObjectName("clearButton")
        self.equalButton = QtGui.QPushButton(self.centralwidget)
        self.equalButton.setGeometry(QtCore.QRect(227, 223, 55, 40))
        self.equalButton.setObjectName("equalButton")
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 271, 51))
        self.textEdit.setObjectName("textEdit")
        self.dotButton = QtGui.QPushButton(self.centralwidget)
        self.dotButton.setGeometry(QtCore.QRect(65, 223, 55, 40))
        self.dotButton.setObjectName("dotButton")
        self.mrButton = QtGui.QPushButton(self.centralwidget)
        self.mrButton.setGeometry(QtCore.QRect(65, 67, 55, 40))
        self.mrButton.setObjectName("mrButton")
        self.mmButton = QtGui.QPushButton(self.centralwidget)
        self.mmButton.setGeometry(QtCore.QRect(173, 67, 55, 40))
        self.mmButton.setObjectName("mmButton")
        self.oneButton = QtGui.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(11, 184, 55, 40))
        self.oneButton.setObjectName("oneButton")
        self.signButton = QtGui.QPushButton(self.centralwidget)
        self.signButton.setGeometry(QtCore.QRect(119, 223, 55, 40))
        self.signButton.setObjectName("signButton")
        self.twoButton = QtGui.QPushButton(self.centralwidget)
        self.twoButton.setGeometry(QtCore.QRect(65, 184, 55, 40))
        self.twoButton.setObjectName("twoButton")
        self.sixButton = QtGui.QPushButton(self.centralwidget)
        self.sixButton.setGeometry(QtCore.QRect(119, 145, 55, 40))
        self.sixButton.setObjectName("sixButton")
        self.eightButton = QtGui.QPushButton(self.centralwidget)
        self.eightButton.setGeometry(QtCore.QRect(65, 106, 55, 40))
        self.eightButton.setObjectName("eightButton")
        self.mcButton = QtGui.QPushButton(self.centralwidget)
        self.mcButton.setGeometry(QtCore.QRect(11, 67, 55, 40))
        self.mcButton.setObjectName("mcButton")
        self.minusButton = QtGui.QPushButton(self.centralwidget)
        self.minusButton.setGeometry(QtCore.QRect(173, 184, 55, 40))
        self.minusButton.setObjectName("minusButton")
        self.addButton = QtGui.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(173, 223, 55, 40))
        self.addButton.setObjectName("addButton")
        self.divideButton = QtGui.QPushButton(self.centralwidget)
        self.divideButton.setGeometry(QtCore.QRect(173, 106, 55, 40))
        self.divideButton.setObjectName("divideButton")
        self.fiveButton = QtGui.QPushButton(self.centralwidget)
        self.fiveButton.setGeometry(QtCore.QRect(65, 145, 55, 40))
        self.fiveButton.setObjectName("fiveButton")
        self.fourButton = QtGui.QPushButton(self.centralwidget)
        self.fourButton.setGeometry(QtCore.QRect(11, 145, 55, 40))
        self.fourButton.setObjectName("fourButton")
        self.sqrtButton = QtGui.QPushButton(self.centralwidget)
        self.sqrtButton.setGeometry(QtCore.QRect(227, 67, 55, 40))
        self.sqrtButton.setObjectName("sqrtButton")
        self.percentButton = QtGui.QPushButton(self.centralwidget)
        self.percentButton.setGeometry(QtCore.QRect(227, 106, 55, 40))
        self.percentButton.setObjectName("percentButton")
        self.mpButton = QtGui.QPushButton(self.centralwidget)
        self.mpButton.setGeometry(QtCore.QRect(119, 67, 55, 40))
        self.mpButton.setObjectName("mpButton")
        self.threeButton = QtGui.QPushButton(self.centralwidget)
        self.threeButton.setGeometry(QtCore.QRect(119, 184, 55, 40))
        self.threeButton.setObjectName("threeButton")
        self.nineButton = QtGui.QPushButton(self.centralwidget)
        self.nineButton.setGeometry(QtCore.QRect(119, 106, 55, 40))
        self.nineButton.setObjectName("nineButton")
        self.zeroButton = QtGui.QPushButton(self.centralwidget)
        self.zeroButton.setGeometry(QtCore.QRect(11, 223, 55, 40))
        self.zeroButton.setObjectName("zeroButton")
        self.sevenButton = QtGui.QPushButton(self.centralwidget)
        self.sevenButton.setGeometry(QtCore.QRect(11, 106, 55, 40))
        self.sevenButton.setObjectName("sevenButton")
        self.multiplyButton = QtGui.QPushButton(self.centralwidget)
        self.multiplyButton.setGeometry(QtCore.QRect(173, 145, 55, 40))
        self.multiplyButton.setObjectName("multiplyButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 291, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.inverseButton.setText(QtGui.QApplication.translate("MainWindow", "1/x", None, QtGui.QApplication.UnicodeUTF8))
        self.clearButton.setText(QtGui.QApplication.translate("MainWindow", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.equalButton.setText(QtGui.QApplication.translate("MainWindow", "=", None, QtGui.QApplication.UnicodeUTF8))
        self.dotButton.setText(QtGui.QApplication.translate("MainWindow", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.mrButton.setText(QtGui.QApplication.translate("MainWindow", "MR", None, QtGui.QApplication.UnicodeUTF8))
        self.mmButton.setText(QtGui.QApplication.translate("MainWindow", "M-", None, QtGui.QApplication.UnicodeUTF8))
        self.oneButton.setText(QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.signButton.setText(QtGui.QApplication.translate("MainWindow", "+/-", None, QtGui.QApplication.UnicodeUTF8))
        self.twoButton.setText(QtGui.QApplication.translate("MainWindow", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.sixButton.setText(QtGui.QApplication.translate("MainWindow", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.eightButton.setText(QtGui.QApplication.translate("MainWindow", "8", None, QtGui.QApplication.UnicodeUTF8))
        self.mcButton.setText(QtGui.QApplication.translate("MainWindow", "MC", None, QtGui.QApplication.UnicodeUTF8))
        self.minusButton.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.divideButton.setText(QtGui.QApplication.translate("MainWindow", "÷", None, QtGui.QApplication.UnicodeUTF8))
        self.fiveButton.setText(QtGui.QApplication.translate("MainWindow", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.fourButton.setText(QtGui.QApplication.translate("MainWindow", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.sqrtButton.setText(QtGui.QApplication.translate("MainWindow", "√", None, QtGui.QApplication.UnicodeUTF8))
        self.percentButton.setText(QtGui.QApplication.translate("MainWindow", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.mpButton.setText(QtGui.QApplication.translate("MainWindow", "M+", None, QtGui.QApplication.UnicodeUTF8))
        self.threeButton.setText(QtGui.QApplication.translate("MainWindow", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.nineButton.setText(QtGui.QApplication.translate("MainWindow", "9", None, QtGui.QApplication.UnicodeUTF8))
        self.zeroButton.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.sevenButton.setText(QtGui.QApplication.translate("MainWindow", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.multiplyButton.setText(QtGui.QApplication.translate("MainWindow", "×", None, QtGui.QApplication.UnicodeUTF8))

