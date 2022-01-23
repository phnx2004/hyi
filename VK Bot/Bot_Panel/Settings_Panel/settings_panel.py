# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(761, 332)
        self.Window = QtWidgets.QFrame(Form)
        self.Window.setGeometry(QtCore.QRect(10, 10, 741, 311))
        self.Window.setStyleSheet("QFrame{\n"
"    border-radius: 7px;\n"
"    background-color: #1B1D23;\n"
"}\n"
"\n"
"QLabel{\n"
"    color: white;\n"
"}")
        self.Window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Window.setObjectName("Window")
        self.WindowFrame = QtWidgets.QFrame(self.Window)
        self.WindowFrame.setGeometry(QtCore.QRect(0, 0, 741, 31))
        self.WindowFrame.setStyleSheet("QFrame{\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    background-color: #2C313C;\n"
"}")
        self.WindowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.WindowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.WindowFrame.setObjectName("WindowFrame")
        self.CloseWindowButton = QtWidgets.QPushButton(self.WindowFrame)
        self.CloseWindowButton.setGeometry(QtCore.QRect(701, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CloseWindowButton.setFont(font)
        self.CloseWindowButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseWindowButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.CloseWindowButton.setObjectName("CloseWindowButton")
        self.MinimizeWindowButton = QtWidgets.QPushButton(self.WindowFrame)
        self.MinimizeWindowButton.setGeometry(QtCore.QRect(660, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.MinimizeWindowButton.setFont(font)
        self.MinimizeWindowButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MinimizeWindowButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.MinimizeWindowButton.setDefault(False)
        self.MinimizeWindowButton.setObjectName("MinimizeWindowButton")
        self.SaveBotSettingsButton = QtWidgets.QPushButton(self.WindowFrame)
        self.SaveBotSettingsButton.setGeometry(QtCore.QRect(629, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SaveBotSettingsButton.setFont(font)
        self.SaveBotSettingsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SaveBotSettingsButton.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}")
        self.SaveBotSettingsButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/SaveOff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveBotSettingsButton.setIcon(icon)
        self.SaveBotSettingsButton.setIconSize(QtCore.QSize(25, 25))
        self.SaveBotSettingsButton.setObjectName("SaveBotSettingsButton")
        self.VKTokenLineEdit = QtWidgets.QLineEdit(self.Window)
        self.VKTokenLineEdit.setGeometry(QtCore.QRect(20, 50, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VKTokenLineEdit.setFont(font)
        self.VKTokenLineEdit.setStyleSheet("QLineEdit{\n"
"    border-bottom-left-radius: 12px;\n"
"    border-top-left-radius: 12px;\n"
"}")
        self.VKTokenLineEdit.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.VKTokenLineEdit.setInputMask("")
        self.VKTokenLineEdit.setText("")
        self.VKTokenLineEdit.setFrame(False)
        self.VKTokenLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.VKTokenLineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.VKTokenLineEdit.setObjectName("VKTokenLineEdit")
        self.IDBotLineEdit = QtWidgets.QLineEdit(self.Window)
        self.IDBotLineEdit.setGeometry(QtCore.QRect(20, 100, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.IDBotLineEdit.setFont(font)
        self.IDBotLineEdit.setStyleSheet("QLineEdit{\n"
"    border-radius: 12px;\n"
"}")
        self.IDBotLineEdit.setInputMask("")
        self.IDBotLineEdit.setText("")
        self.IDBotLineEdit.setFrame(False)
        self.IDBotLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.IDBotLineEdit.setDragEnabled(False)
        self.IDBotLineEdit.setReadOnly(False)
        self.IDBotLineEdit.setObjectName("IDBotLineEdit")
        self.frame = QtWidgets.QFrame(self.Window)
        self.frame.setGeometry(QtCore.QRect(350, 50, 41, 41))
        self.frame.setStyleSheet("QFrame{\n"
"    border-bottom-right-radius: 12px;\n"
"    border-top-right-radius: 12px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-top-left-radius: 0px;\n"
"    background-color: white;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ShowVKTokenButton = QtWidgets.QPushButton(self.frame)
        self.ShowVKTokenButton.setGeometry(QtCore.QRect(0, 0, 41, 41))
        self.ShowVKTokenButton.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"}")
        self.ShowVKTokenButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Icons/eyeOn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ShowVKTokenButton.setIcon(icon1)
        self.ShowVKTokenButton.setIconSize(QtCore.QSize(32, 32))
        self.ShowVKTokenButton.setObjectName("ShowVKTokenButton")
        self.label = QtWidgets.QLabel(self.Window)
        self.label.setGeometry(QtCore.QRect(400, 47, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.AutomatiAuthorizatonButton = QtWidgets.QPushButton(self.Window)
        self.AutomatiAuthorizatonButton.setGeometry(QtCore.QRect(700, 50, 20, 21))
        self.AutomatiAuthorizatonButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AutomatiAuthorizatonButton.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"}")
        self.AutomatiAuthorizatonButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Icons/Off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AutomatiAuthorizatonButton.setIcon(icon2)
        self.AutomatiAuthorizatonButton.setIconSize(QtCore.QSize(16, 16))
        self.AutomatiAuthorizatonButton.setObjectName("AutomatiAuthorizatonButton")
        self.label_2 = QtWidgets.QLabel(self.Window)
        self.label_2.setGeometry(QtCore.QRect(400, 87, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.UserCommandsButton = QtWidgets.QPushButton(self.Window)
        self.UserCommandsButton.setGeometry(QtCore.QRect(684, 90, 20, 21))
        self.UserCommandsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.UserCommandsButton.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"}")
        self.UserCommandsButton.setText("")
        self.UserCommandsButton.setIcon(icon2)
        self.UserCommandsButton.setIconSize(QtCore.QSize(16, 16))
        self.UserCommandsButton.setObjectName("UserCommandsButton")
        self.AddUserCommandButton = QtWidgets.QPushButton(self.Window)
        self.AddUserCommandButton.setGeometry(QtCore.QRect(400, 150, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.AddUserCommandButton.setFont(font)
        self.AddUserCommandButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AddUserCommandButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")
        self.AddUserCommandButton.setObjectName("AddUserCommandButton")
        self.UserCommandsListWidget = QtWidgets.QListWidget(self.Window)
        self.UserCommandsListWidget.setGeometry(QtCore.QRect(20, 150, 371, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.UserCommandsListWidget.setFont(font)
        self.UserCommandsListWidget.setTabletTracking(False)
        self.UserCommandsListWidget.setAutoFillBackground(False)
        self.UserCommandsListWidget.setStyleSheet("color: white;\n"
"border-radius: 7px;\n"
"background-color: #2C313C;\n"
"")
        self.UserCommandsListWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.UserCommandsListWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.UserCommandsListWidget.setLineWidth(1)
        self.UserCommandsListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.UserCommandsListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.UserCommandsListWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.UserCommandsListWidget.setAutoScroll(True)
        self.UserCommandsListWidget.setTabKeyNavigation(False)
        self.UserCommandsListWidget.setProperty("showDropIndicator", True)
        self.UserCommandsListWidget.setDragDropOverwriteMode(False)
        self.UserCommandsListWidget.setAlternatingRowColors(False)
        self.UserCommandsListWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.UserCommandsListWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.UserCommandsListWidget.setMovement(QtWidgets.QListView.Static)
        self.UserCommandsListWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.UserCommandsListWidget.setProperty("isWrapping", False)
        self.UserCommandsListWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.UserCommandsListWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.UserCommandsListWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.UserCommandsListWidget.setUniformItemSizes(False)
        self.UserCommandsListWidget.setWordWrap(False)
        self.UserCommandsListWidget.setSelectionRectVisible(False)
        self.UserCommandsListWidget.setObjectName("UserCommandsListWidget")
        self.DeleteUserCommandButton = QtWidgets.QPushButton(self.Window)
        self.DeleteUserCommandButton.setGeometry(QtCore.QRect(400, 250, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.DeleteUserCommandButton.setFont(font)
        self.DeleteUserCommandButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DeleteUserCommandButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")
        self.DeleteUserCommandButton.setObjectName("DeleteUserCommandButton")
        self.EditUserCommandButton = QtWidgets.QPushButton(self.Window)
        self.EditUserCommandButton.setGeometry(QtCore.QRect(400, 200, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.EditUserCommandButton.setFont(font)
        self.EditUserCommandButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EditUserCommandButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")
        self.EditUserCommandButton.setObjectName("EditUserCommandButton")
        self.label_3 = QtWidgets.QLabel(self.Window)
        self.label_3.setGeometry(QtCore.QRect(400, 67, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.AutomatiSaveLogButton = QtWidgets.QPushButton(self.Window)
        self.AutomatiSaveLogButton.setGeometry(QtCore.QRect(678, 70, 20, 21))
        self.AutomatiSaveLogButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AutomatiSaveLogButton.setStyleSheet("QPushButton{\n"
"    border: none;\n"
"}")
        self.AutomatiSaveLogButton.setText("")
        self.AutomatiSaveLogButton.setIcon(icon2)
        self.AutomatiSaveLogButton.setIconSize(QtCore.QSize(16, 16))
        self.AutomatiSaveLogButton.setObjectName("AutomatiSaveLogButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.CloseWindowButton.setText(_translate("Form", "X"))
        self.MinimizeWindowButton.setText(_translate("Form", "_"))
        self.VKTokenLineEdit.setPlaceholderText(_translate("Form", "Введите VK Token бота"))
        self.IDBotLineEdit.setPlaceholderText(_translate("Form", "Введите ID бота"))
        self.label.setText(_translate("Form", "Автоматическая авторизация:"))
        self.label_2.setText(_translate("Form", "Пользовательские команды:"))
        self.AddUserCommandButton.setText(_translate("Form", "Добавить команду"))
        self.UserCommandsListWidget.setSortingEnabled(False)
        self.DeleteUserCommandButton.setText(_translate("Form", "Удалить команду"))
        self.EditUserCommandButton.setText(_translate("Form", "Изменить команду"))
        self.label_3.setText(_translate("Form", "Автомат. сохранение логов:"))
