# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

# 这些代码都是自动生成的。
# 在生成的文件中有一个Ui_MainWindow类，这个类继承自object，这个类就是一个空的类，里面什么都没有，就是提供了一个容器，
# 在容器内部生成了一个名字叫MainWindow的对象，设置对象的大小，然后将这个对象MainWindow作为父类生成了一个子对象 centralwidget。
# centralwidget作为这个容器类的内部成员，这个对象centralwidget就是将来程序要运行的主窗口，
# 在这个窗口内部放置了很多的控件，具体不详细论述了。
# 函数retranslateUi(self, MainWindow)的主要作用是设置控件的各种属性

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(170, 410, 101, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 410, 101, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 100, 341, 231))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_2, self.pushButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "first1"))
        self.pushButton.setText(_translate("MainWindow", "点击1"))
        self.pushButton_2.setText(_translate("MainWindow", "点击2"))

