# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from functions import call_screen, show_message, login
from cadastro import Ui_Cadastro
from principal import Ui_Principal


class Ui_Login(QtWidgets.QDialog):
    def setupUi(self):
        self.setObjectName("login")
        self.resize(355, 500)
        self.setMinimumSize(QtCore.QSize(355, 500))
        self.setMaximumSize(QtCore.QSize(355, 500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/closed_book_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.senha = QtWidgets.QLabel(self)
        self.senha.setGeometry(QtCore.QRect(30, 320, 111, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.senha.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.senha.setFont(font)
        self.senha.setObjectName("senha")
        self.campousuario = QtWidgets.QLineEdit(self)
        self.campousuario.setGeometry(QtCore.QRect(130, 270, 180, 20))
        self.campousuario.setObjectName("campousuario")
        self.camposenha = QtWidgets.QLineEdit(self)
        self.camposenha.setGeometry(QtCore.QRect(130, 320, 180, 20))
        self.camposenha.setObjectName("camposenha")
        self.camposenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.usuario = QtWidgets.QLabel(self)
        self.usuario.setGeometry(QtCore.QRect(30, 270, 111, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.usuario.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.usuario.setFont(font)
        self.usuario.setObjectName("usuario")
        self.livro = QtWidgets.QLabel(self)
        self.livro.setGeometry(QtCore.QRect(60, 20, 231, 220))
        self.livro.setText("")
        self.livro.setPixmap(QtGui.QPixmap("resources/closed_book_image.png"))
        self.livro.setScaledContents(True)
        self.livro.setObjectName("livro")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.blogar = QtWidgets.QPushButton(self)
        self.blogar.setGeometry(QtCore.QRect(120, 370, 110, 30))
        self.bcriarconta = QtWidgets.QPushButton(self)
        self.bcriarconta.setGeometry(QtCore.QRect(90, 450, 171, 25))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.blogar.setPalette(palette)
        self.blogar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.blogar.setObjectName("blogar")
        self.bcriarconta.setPalette(palette)
        self.bcriarconta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bcriarconta.setObjectName("bcriarconta")
        self.retranslateUi()

        self.bcriarconta.clicked.connect(self.signup_screen)
        self.blogar.clicked.connect(self.verify)
        QtCore.QMetaObject.connectSlotsByName(self)


    def signup_screen(self):
        call_screen(self, Ui_Cadastro())


    def verify(self):
        if login(self):
            call_screen(self, Ui_Principal())
        else: pass


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("login", "Login"))
        self.senha.setText(_translate("login", "    Senha"))
        self.usuario.setText(_translate("login", "  Usuário"))
        self.bcriarconta.setText(_translate("login", "Criar uma conta"))
        self.blogar.setText(_translate("login", "Logar"))
