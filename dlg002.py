# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '002.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

# Tinelix IRC Client for PyQt5
# Licensed by GPLv3.

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(307, 105)
        Dialog.setMinimumSize(QtCore.QSize(200, 105))
        Dialog.setMaximumSize(QtCore.QSize(400, 105))
        Dialog.setStyleSheet("background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setStyleSheet("selection-background-color: rgb(161, 75, 0);")
        self.lineEdit.setMaxLength(40)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.profname = QtWidgets.QLabel(Dialog)
        self.profname.setText("")
        self.profname.setObjectName("profname")
        self.verticalLayout.addWidget(self.profname)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setMinimumSize(QtCore.QSize(33, 33))
        self.buttonBox.setStyleSheet("selection-background-color: rgb(255, 119, 0);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Имя профиля:"))
