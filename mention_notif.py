# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mention_notif.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(313, 128)
        Dialog.setStyleSheet("background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nickname_label = QtWidgets.QLabel(Dialog)
        self.nickname_label.setMinimumSize(QtCore.QSize(0, 19))
        self.nickname_label.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nickname_label.setFont(font)
        self.nickname_label.setObjectName("nickname_label")
        self.horizontalLayout_2.addWidget(self.nickname_label)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(16, 16))
        self.label_2.setMaximumSize(QtCore.QSize(16, 16))
        self.label_2.setStyleSheet("image: url(:/button_icons/closebutton.png);")
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.msg_text = QtWidgets.QLabel(Dialog)
        self.msg_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.msg_text.setWordWrap(True)
        self.msg_text.setObjectName("msg_text")
        self.verticalLayout.addWidget(self.msg_text)
        self.openclient_btn = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.openclient_btn.setFont(font)
        self.openclient_btn.setDefault(False)
        self.openclient_btn.setFlat(True)
        self.openclient_btn.setObjectName("openclient_btn")
        self.verticalLayout.addWidget(self.openclient_btn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Уведомление"))
        self.nickname_label.setText(_translate("Dialog", "какой-то никнейм упомянул вас"))
        self.msg_text.setText(_translate("Dialog", "tinelix ладно."))
        self.openclient_btn.setText(_translate("Dialog", "Открыть"))
import resources_rc
