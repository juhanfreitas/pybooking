# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from functions import call_screen
from buscar import Ui_Buscar
from dados import Ui_Dados
from ajuda import Ui_Ajuda
from devolucao import Ui_Devolucao
from creditos import Ui_Creditos

import sys

class Ui_Principal(QtWidgets.QMainWindow):
    def setupUi(self):
        self.setObjectName("principal")
        self.resize(800, 450)
        self.setMinimumSize(QtCore.QSize(800, 450))
        self.setMaximumSize(QtCore.QSize(800, 450))
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
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 300, 521, 31))
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
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.bbuscar = QtWidgets.QPushButton(self.centralwidget)
        self.bbuscar.setGeometry(QtCore.QRect(280, 350, 241, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(172, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(172, 50, 50))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.bbuscar.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.bbuscar.setFont(font)
        self.bbuscar.setObjectName("bbuscar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 20, 271, 40))
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
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 40, 260, 260))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("resources/alpha_image.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuUsu_rio = QtWidgets.QMenu(self.menuArquivo)
        self.menuUsu_rio.setObjectName("menuUsu_rio")
        self.menuSobre = QtWidgets.QMenu(self.menubar)
        self.menuSobre.setObjectName("menuSobre")
        self.setMenuBar(self.menubar)
        self.actionEmprestimos = QtWidgets.QAction(self)
        self.actionEmprestimos.setObjectName("actionEmprestimos")
        self.actionDevolu_es = QtWidgets.QAction(self)
        self.actionDevolu_es.setObjectName("actionDevolu_es")
        self.actionLogout = QtWidgets.QAction(self)
        self.actionLogout.setObjectName("actionLogout")
        self.actionSair = QtWidgets.QAction(self)
        self.actionSair.setObjectName("actionSair")
        self.actionAjuda = QtWidgets.QAction(self)
        self.actionAjuda.setObjectName("actionAjuda")
        self.actionCr_ditos = QtWidgets.QAction(self)
        self.actionCr_ditos.setObjectName("actionCr_ditos")
        self.actionEmpr_stimos = QtWidgets.QAction(self)
        self.actionEmpr_stimos.setObjectName("actionEmpr_stimos")
        self.actionDados = QtWidgets.QAction(self)
        self.actionDados.setObjectName("actionDados")
        self.menuUsu_rio.addAction(self.actionDevolu_es)
        self.menuUsu_rio.addSeparator()
        self.menuUsu_rio.addAction(self.actionDados)
        self.menuArquivo.addAction(self.menuUsu_rio.menuAction())
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionLogout)
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionSair)
        self.menuSobre.addAction(self.actionAjuda)
        self.menuSobre.addSeparator()
        self.menuSobre.addAction(self.actionCr_ditos)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi()

        self.actionSair.triggered.connect(self.call_exit)
        self.bbuscar.clicked.connect(self.call_buscar)
        self.actionCr_ditos.triggered.connect(self.call_creditos)
        self.actionLogout.triggered.connect(self.login_screen)
        self.actionDados.triggered.connect(self.call_dados)
        self.actionAjuda.triggered.connect(self.call_ajuda)
        self.actionDevolu_es.triggered.connect(self.call_devolucao)
        QtCore.QMetaObject.connectSlotsByName(self)


    def call_buscar(self):
        call_screen(self, Ui_Buscar(), hide=False)


    def login_screen(self):
        from login import Ui_Login
        call_screen(self, Ui_Login())


    def call_creditos(self):
        call_screen(self, Ui_Creditos(), hide=False)


    def call_dados(self):
        call_screen(self, Ui_Dados(), hide=False)


    def call_ajuda(self):
        call_screen(self, Ui_Ajuda(), hide=False)

    
    def call_devolucao(self):
        call_screen(self, Ui_Devolucao(), hide=False)
        

    def call_exit(self):
        sys.exit(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("principal", "Pybooking - Início"))
        self.label.setText(_translate("principal", "Clique abaixo para buscar um livro em nosso acervo"))
        self.bbuscar.setText(_translate("principal", "Buscar Livro"))
        self.label_2.setText(_translate("principal", "Bem vindo ao Pybooking"))
        self.menuArquivo.setTitle(_translate("principal", "Arquivo"))
        self.menuUsu_rio.setTitle(_translate("principal", "Usuário"))
        self.menuSobre.setTitle(_translate("principal", "Sobre"))
        self.actionEmprestimos.setText(_translate("principal", "Emprestimos"))
        self.actionDevolu_es.setText(_translate("principal", "Devoluções"))
        self.actionLogout.setText(_translate("principal", "Logout"))
        self.actionSair.setText(_translate("principal", "Sair"))
        self.actionAjuda.setText(_translate("principal", "Ajuda..."))
        self.actionCr_ditos.setText(_translate("principal", "Créditos"))
        self.actionEmpr_stimos.setText(_translate("principal", "Empréstimos"))
        self.actionDados.setText(_translate("principal", "Dados"))
