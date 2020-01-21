# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from functions import signup, call_screen, show_message
from principal import Ui_Principal


class Ui_Cadastro(QtWidgets.QDialog):
    def setupUi(self):
        from login import Ui_Login
        self.setObjectName("Cadastro")
        self.resize(500, 700)
        self.setMinimumSize(QtCore.QSize(500, 680))
        self.setMaximumSize(QtCore.QSize(500, 680))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/closed_book_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.nome = QtWidgets.QLabel(self)
        self.nome.setGeometry(QtCore.QRect(76, 250, 91, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.nome.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        self.nome.setFont(font)
        self.nome.setObjectName("nome")
        self.camponome = QtWidgets.QLineEdit(self)
        self.camponome.setGeometry(QtCore.QRect(190, 250, 201, 21))
        self.camponome.setObjectName("camponome")
        self.campotelefone = QtWidgets.QLineEdit(self)
        self.campotelefone.setGeometry(QtCore.QRect(190, 320, 201, 21))
        self.campotelefone.setObjectName("campotelefone")
        self.telefone = QtWidgets.QLabel(self)
        self.telefone.setGeometry(QtCore.QRect(80, 320, 91, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.telefone.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        self.telefone.setFont(font)
        self.telefone.setObjectName("telefone")
        self.campoemail = QtWidgets.QLineEdit(self)
        self.campoemail.setGeometry(QtCore.QRect(190, 390, 201, 21))
        self.campoemail.setObjectName("campoemail")
        self.email = QtWidgets.QLabel(self)
        self.email.setGeometry(QtCore.QRect(80, 390, 91, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.email.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.campousuario = QtWidgets.QLineEdit(self)
        self.campousuario.setGeometry(QtCore.QRect(190, 460, 201, 21))
        self.campousuario.setObjectName("campousuario")
        self.user = QtWidgets.QLabel(self)
        self.user.setGeometry(QtCore.QRect(80, 460, 91, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.user.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        self.user.setFont(font)
        self.user.setObjectName("user")
        self.camposenha = QtWidgets.QLineEdit(self)
        self.camposenha.setGeometry(QtCore.QRect(190, 530, 201, 21))
        self.camposenha.setObjectName("camposenha")
        self.camposenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.senha = QtWidgets.QLabel(self)
        self.senha.setGeometry(QtCore.QRect(80, 530, 91, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(33, 37, 95))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.senha.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        self.senha.setFont(font)
        self.senha.setObjectName("senha")
        self.icon = QtWidgets.QLabel(self)
        self.icon.setGeometry(QtCore.QRect(130, 0, 250, 250))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("resources/closed_book_image.png"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.bcadastrar = QtWidgets.QPushButton(self)
        self.bcadastrar.setGeometry(QtCore.QRect(190, 575, 120, 40))
        self.bcadastrar.setObjectName("bcadastrar")
        self.btnlogin = QtWidgets.QPushButton(self)
        self.btnlogin.setGeometry(QtCore.QRect(175, 633, 150, 25))
        self.btnlogin.setObjectName("btnlogin")
        self.retranslateUi()

        self.bcadastrar.clicked.connect(self.salvarCliente)
        self.btnlogin.clicked.connect(self.login_screen)
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Cadastro", "Cadastro"))
        self.nome.setText(_translate("Cadastro", "     Nome:"))
        self.telefone.setText(_translate("Cadastro", "  Telefone:"))
        self.email.setText(_translate("Cadastro", "    E-mail:"))
        self.user.setText(_translate("Cadastro", "   Usuário:"))
        self.senha.setText(_translate("Cadastro", "     Senha:"))
        self.btnlogin.setText(_translate("Cadastro", "Login"))
        self.bcadastrar.setText(_translate("Cadastro", "Cadastrar"))


    def login_screen(self):
        from login import Ui_Login
        call_screen(self, Ui_Login())


    def salvarCliente(self):
        if str(self.camponome.text()) == "" or str(self.campotelefone.text()) == "" or str(self.campoemail.text())=="" or str(self.campousuario.text())=="" or str(self.camposenha.text()) == "":
            show_message("Aviso", QtWidgets.QMessageBox.Warning, "Um ou mais campos não foram preenchidos")
            self.apagaCampos()

        else:
            try:
                failed_to_signed_up = signup(
                    self.camponome.text(),
                    self.campotelefone.text(),
                    self.campoemail.text(),
                    self.campousuario.text(),
                    self.camposenha.text()
                )

                if not failed_to_signed_up:
                    show_message("Sucesso", QtWidgets.QMessageBox.Information, "Cliente cadastrado com sucesso")

                    call_screen(self, Ui_Principal())

            except Exception:
                show_message("Erro", QtWidgets.QMessageBox.Critical, "Erro ao cadastrar o cliente")

            self.apagaCampos()

    
    def apagaCampos(self):
        self.campoemail.clear()
        self.camponome.clear()
        self.campotelefone.clear()
        self.campousuario.clear()
        self.camposenha.clear()
