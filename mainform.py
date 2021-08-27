# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 354)
        MainWindow.setMinimumSize(QtCore.QSize(544, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon_48x48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(43, 43, 43);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dialogs_list = QtWidgets.QListView(self.centralwidget)
        self.dialogs_list.setMinimumSize(QtCore.QSize(128, 0))
        self.dialogs_list.setMaximumSize(QtCore.QSize(112, 16777215))
        self.dialogs_list.setStyleSheet("selection-background-color: rgb(161, 75, 0);")
        self.dialogs_list.setObjectName("dialogs_list")
        self.horizontalLayout.addWidget(self.dialogs_list)
        self.chat_text = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.chat_text.setFont(font)
        self.chat_text.setStyleSheet("selection-background-color: rgb(161, 75, 0);")
        self.chat_text.setUndoRedoEnabled(False)
        self.chat_text.setReadOnly(True)
        self.chat_text.setObjectName("chat_text")
        self.horizontalLayout.addWidget(self.chat_text)
        self.members_list = QtWidgets.QTreeWidget(self.centralwidget)
        self.members_list.setMinimumSize(QtCore.QSize(144, 0))
        self.members_list.setMaximumSize(QtCore.QSize(144, 16777215))
        self.members_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.members_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.members_list.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.members_list.setIndentation(10)
        self.members_list.setRootIsDecorated(False)
        self.members_list.setAnimated(False)
        self.members_list.setWordWrap(True)
        self.members_list.setExpandsOnDoubleClick(True)
        self.members_list.setObjectName("members_list")
        self.members_list.header().setVisible(False)
        self.horizontalLayout.addWidget(self.members_list)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.message_text = QtWidgets.QLineEdit(self.centralwidget)
        self.message_text.setEnabled(False)
        self.message_text.setStyleSheet("selection-background-color: rgb(161, 75, 0);\n"
"color: rgb(79, 79, 79);")
        self.message_text.setObjectName("message_text")
        self.horizontalLayout_2.addWidget(self.message_text)
        self.send_msg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.send_msg_btn.setEnabled(False)
        self.send_msg_btn.setStyleSheet("border-color: rgb(255, 119, 0); selection-background-color: rgb(255, 119, 0); color: #4f4f4f")
        self.send_msg_btn.setObjectName("send_msg_btn")
        self.horizontalLayout_2.addWidget(self.send_msg_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setMinimumSize(QtCore.QSize(100, 0))
        self.status_label.setMaximumSize(QtCore.QSize(220, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.status_label.setFont(font)
        self.status_label.setText("")
        self.status_label.setTextFormat(QtCore.Qt.PlainText)
        self.status_label.setObjectName("status_label")
        self.horizontalLayout_3.addWidget(self.status_label)
        spacerItem = QtWidgets.QSpacerItem(2, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.channel_name = QtWidgets.QLabel(self.centralwidget)
        self.channel_name.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.channel_name.setFont(font)
        self.channel_name.setText("")
        self.channel_name.setObjectName("channel_name")
        self.horizontalLayout_3.addWidget(self.channel_name)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setStyleSheet("color: rgb(74, 74, 74)")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.conn_quality_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.conn_quality_label.setFont(font)
        self.conn_quality_label.setObjectName("conn_quality_label")
        self.horizontalLayout_3.addWidget(self.conn_quality_label)
        self.conn_quality_progr = QtWidgets.QProgressBar(self.centralwidget)
        self.conn_quality_progr.setMinimumSize(QtCore.QSize(0, 18))
        self.conn_quality_progr.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.conn_quality_progr.setFont(font)
        self.conn_quality_progr.setStyleSheet("selection-background-color: rgb(161, 75, 0);")
        self.conn_quality_progr.setMaximum(5000)
        self.conn_quality_progr.setProperty("value", 4970)
        self.conn_quality_progr.setTextVisible(True)
        self.conn_quality_progr.setInvertedAppearance(False)
        self.conn_quality_progr.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.conn_quality_progr.setObjectName("conn_quality_progr")
        self.horizontalLayout_3.addWidget(self.conn_quality_progr)
        self.latency_label = QtWidgets.QLabel(self.centralwidget)
        self.latency_label.setMinimumSize(QtCore.QSize(35, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.latency_label.setFont(font)
        self.latency_label.setObjectName("latency_label")
        self.horizontalLayout_3.addWidget(self.latency_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 595, 29))
        self.menubar.setStyleSheet("selection-background-color: rgb(161, 75, 0);")
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setStyleSheet("")
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.about_item = QtWidgets.QAction(MainWindow)
        self.about_item.setObjectName("about_item")
        self.about_Qt_item = QtWidgets.QAction(MainWindow)
        self.about_Qt_item.setObjectName("about_Qt_item")
        self.connect_item = QtWidgets.QAction(MainWindow)
        self.connect_item.setObjectName("connect_item")
        self.quit_item = QtWidgets.QAction(MainWindow)
        self.quit_item.setObjectName("quit_item")
        self.history_cb_action = QtWidgets.QAction(MainWindow)
        self.history_cb_action.setCheckable(True)
        self.history_cb_action.setChecked(False)
        self.history_cb_action.setObjectName("history_cb_action")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.settings_item = QtWidgets.QAction(MainWindow)
        self.settings_item.setObjectName("settings_item")
        self.menu.addAction(self.connect_item)
        self.menu.addSeparator()
        self.menu.addAction(self.quit_item)
        self.menu_2.addAction(self.about_item)
        self.menu_3.addAction(self.settings_item)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tinelix IRC Client"))
        self.members_list.headerItem().setText(0, _translate("MainWindow", "Members"))
        self.message_text.setText(_translate("MainWindow", "На данный момент отправить сообщение нельзя"))
        self.send_msg_btn.setText(_translate("MainWindow", "Отправить"))
        self.conn_quality_label.setText(_translate("MainWindow", "Качество соединения:"))
        self.conn_quality_progr.setFormat(_translate("MainWindow", "%p%"))
        self.latency_label.setText(_translate("MainWindow", "(2 ms)"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Справка"))
        self.menu_3.setTitle(_translate("MainWindow", "Вид"))
        self.about_item.setText(_translate("MainWindow", "О программе..."))
        self.about_Qt_item.setText(_translate("MainWindow", "О Qt..."))
        self.connect_item.setText(_translate("MainWindow", "Подключиться"))
        self.quit_item.setText(_translate("MainWindow", "Выход"))
        self.history_cb_action.setText(_translate("MainWindow", "Сохранить историю переписок"))
        self.action.setText(_translate("MainWindow", "Настройки"))
        self.settings_item.setText(_translate("MainWindow", "Настройки"))
import resources_rc
