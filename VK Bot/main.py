# -*- coding: utf-8 -*-

# PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# GUI
import Authorization_Window.authorization_window as authorization_window
import Registration_Window.registration_window as registration_window
from bot_panel_window import BotPanelWindow
from message_box import MessageBox

# Другие
import config as Config
from methods import *
import requests
import json
import sys

# Создание файла "User-Commands.json" для работы бота
if find_file('User-Commands.json') == False:
	with open('User-Commands.json', 'a') as file:
		file.write(json.dumps([], ensure_ascii = False, indent = 2))

# Создание файла "Bot-Settings.json" для работы бота
if find_file('Bot-Settings.json') == False:
	with open('Bot-Settings.json', 'a') as file:
		data = {
			'Automati_Authorizaton': False,
			'Automati_Save_Log': False,
			'User_Commands': False,
			'VK_Token': '',
			'Group_ID': ''
		}
		file.write(json.dumps(data, ensure_ascii = False, indent = 2))

# Графический интерфейс программы
# ==================================================================
class RegistrationWindow(QtWidgets.QMainWindow): # Окно регистрации
	def __init__(self, parent = None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = registration_window.Ui_MainWindow()
		self.ui.setupUi(self)

		# Отключаем стандартные границы окна программы
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.center()

		# Обработчики основных кнопок
		self.ui.ShowPasswordButton.clicked.connect(self.show_password)
		self.ui.CreateAccountButton.clicked.connect(self.create_account)
		self.ui.LoginLineEdit.returnPressed.connect(self.create_account)
		self.ui.PasswordLineEdit.returnPressed.connect(self.create_account)
		self.ui.AskButton.clicked.connect(self.authorization_window)

		# Обработчики кнопок с панели
		self.ui.CloseWindowButton.clicked.connect(lambda: self.close())
		self.ui.MinimizeWindowButton.clicked.connect(lambda: self.showMinimized())

	# Перетаскивание безрамочного окна
	# ==================================================================
	def center(self):
		qr = self.frameGeometry()
		cp = QtWidgets.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()

	def mouseMoveEvent(self, event):
		try:
			delta = QtCore.QPoint(event.globalPos() - self.oldPos)
			self.move(self.x() + delta.x(), self.y() + delta.y())
			self.oldPos = event.globalPos()
		except AttributeError:
			pass
	# ==================================================================

	# Логика основных кнопок
	# ==================================================================
	def show_password(self):
		if self.ui.PasswordLineEdit.echoMode() == 2:
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("../Icons/eyeOff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.ui.ShowPasswordButton.setIcon(icon)
			self.ui.PasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
		else:
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("../Icons/eyeOn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.ui.ShowPasswordButton.setIcon(icon)
			self.ui.PasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

	def create_account(self):
		data = {
			'Login': self.ui.LoginLineEdit.text(),
			'Password': self.ui.PasswordLineEdit.text()
		}
		server_answer = requests.post(f'{Config.SERVER}/vk_bot/registration', json = data)
		server_answer_text = json.loads(server_answer.text)
		if server_answer.status_code == 200:
			auth = AuthorizationWindow()
			self.close()
			auth.show()
		else:
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')

	def authorization_window(self):
		auth = AuthorizationWindow()
		self.close()
		auth.show()

class AuthorizationWindow(QtWidgets.QMainWindow): # Окно авторизации
	def __init__(self, parent = None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = authorization_window.Ui_MainWindow()
		self.ui.setupUi(self)

		# Отключаем стандартные границы окна программы
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		self.center()

		# Обработчики основных кнопок
		self.ui.ShowPasswordButton.clicked.connect(self.show_password)
		self.ui.AuthorizationButton.clicked.connect(self.authorization)
		self.ui.LoginLineEdit.returnPressed.connect(self.authorization)
		self.ui.PasswordLineEdit.returnPressed.connect(self.authorization)
		self.ui.AskButton.clicked.connect(self.registration_window)

		# Обработчики кнопок с панели
		self.ui.CloseWindowButton.clicked.connect(lambda: self.close())
		self.ui.MinimizeWindowButton.clicked.connect(lambda: self.showMinimized())

	# Перетаскивание безрамочного окна
	# ==================================================================
	def center(self):
		qr = self.frameGeometry()
		cp = QtWidgets.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()

	def mouseMoveEvent(self, event):
		try:
			delta = QtCore.QPoint(event.globalPos() - self.oldPos)
			self.move(self.x() + delta.x(), self.y() + delta.y())
			self.oldPos = event.globalPos()
		except AttributeError:
			pass
	# ==================================================================

	# Логика основных кнопок
	# ==================================================================
	def show_password(self):
		if self.ui.PasswordLineEdit.echoMode() == 2:
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("../Icons/eyeOff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.ui.ShowPasswordButton.setIcon(icon)
			self.ui.PasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
		else:
			icon = QtGui.QIcon()
			icon.addPixmap(QtGui.QPixmap("../Icons/eyeOn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
			self.ui.ShowPasswordButton.setIcon(icon)
			self.ui.PasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

	def authorization(self):
		data = {
			'Login': self.ui.LoginLineEdit.text(),
			'Password': self.ui.PasswordLineEdit.text()
		}
		server_answer = requests.post(f'{Config.SERVER}/vk_bot/authorization', json = data)
		server_answer_text = json.loads(server_answer.text)
		if server_answer.status_code == 200:
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')
			Config.UNIQUE_KEY = server_answer_text['Unique_Key']
			bot_panel = BotPanelWindow(self.ui.LoginLineEdit.text(), self.ui.PasswordLineEdit.text())
			self.close()
			bot_panel.show()
		else:
			MessageBox(text = server_answer_text['Answer'], button_2 = 'Окей')

	def registration_window(self):
		reg = RegistrationWindow()
		self.close()
		reg.show()
# ==================================================================

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	bot_settings = get_bot_settings()
	if bot_settings['Automati_Authorizaton'] == True:
		data = {
			'Login': bot_settings['Login'],
			'Password': bot_settings['Password']
		}
		server_answer = requests.post(f'{Config.SERVER}/vk_bot/authorization', json = data)
		server_answer_text = json.loads(server_answer.text)
		if server_answer.status_code == 200:
			Config.UNIQUE_KEY = server_answer_text['Unique_Key']
			myapp = BotPanelWindow(bot_settings['Login'], bot_settings['Password'])
		else:
			bot_settings.update(
				{
					'Automati_Authorizaton': False
				}
			)
			for item in ['Login', 'Password']:
				bot_settings.pop(item)
			with open('Bot-Settings.json', 'wb') as file: 
				file.write(json.dumps(bot_settings, ensure_ascii = False, indent = 2).encode('UTF-8'))
			myapp = AuthorizationWindow()
	else:
		myapp = AuthorizationWindow()
	myapp.show()
	sys.exit(app.exec_())