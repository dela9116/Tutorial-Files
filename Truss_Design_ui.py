# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Truss_Design_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(825, 514)
        self.pushButton_Exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_Exit.setGeometry(QtCore.QRect(330, 380, 112, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_Exit.setFont(font)
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 751, 351))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_GetWing = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_GetWing.setGeometry(QtCore.QRect(10, 30, 241, 34))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_GetWing.setFont(font)
        self.pushButton_GetWing.setObjectName("pushButton_GetWing")
        self.textEdit_filename = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_filename.setGeometry(QtCore.QRect(290, 20, 421, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_filename.setFont(font)
        self.textEdit_filename.setReadOnly(True)
        self.textEdit_filename.setObjectName("textEdit_filename")
        self.textEdit_xAverage = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_xAverage.setGeometry(QtCore.QRect(380, 230, 181, 41))
        self.textEdit_xAverage.setObjectName("textEdit_xAverage")
        self.textEdit_yAverage = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_yAverage.setGeometry(QtCore.QRect(380, 290, 181, 41))
        self.textEdit_yAverage.setObjectName("textEdit_yAverage")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(94, 240, 301, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(90, 300, 301, 20))
        self.label_2.setObjectName("label_2")
        self.textEdit_nNodes = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_nNodes.setGeometry(QtCore.QRect(380, 170, 181, 41))
        self.textEdit_nNodes.setObjectName("textEdit_nNodes")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(140, 180, 301, 20))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Truss Structural Design"))
        self.pushButton_Exit.setText(_translate("Dialog", "Exit"))
        self.groupBox.setTitle(_translate("Dialog", "Truss File"))
        self.pushButton_GetWing.setText(_translate("Dialog", "Open and Read a Truss File"))
        self.label.setText(_translate("Dialog", "Average of x-values for all Nodes"))
        self.label_2.setText(_translate("Dialog", "Average of y-values for all Nodes"))
        self.label_3.setText(_translate("Dialog", "Number of nodes in the file"))

