# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buscar.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from functions import book_database_reader, search_books, borrow_book


class Ui_Buscar(QtWidgets.QDialog):
    def setupUi(self):
        global books, clicked_book
        books = book_database_reader("databases/books.csv")
        clicked_book = []
        self.setObjectName("Buscar")
        self.resize(720, 420)
        self.setMinimumSize(QtCore.QSize(720, 420))
        self.setMaximumSize(QtCore.QSize(720, 420))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/closed_book_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.imagemlivro = QtWidgets.QLabel(self)
        self.imagemlivro.setGeometry(QtCore.QRect(465, 100, 180, 180))
        self.imagemlivro.setText("")
        self.imagemlivro.setScaledContents(True)
        self.imagemlivro.setObjectName("imagemlivro")
        self.imagemlivro.setPixmap(QtGui.QPixmap("resources/alpha_image.png"))
        self.listalivros = QtWidgets.QListWidget(self)
        self.listalivros.setGeometry(QtCore.QRect(20, 100, 370, 280))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(12)
        self.listalivros.setFont(font)
        self.listalivros.setObjectName("listalivros")
        for book in books:
            item = QtWidgets.QListWidgetItem()
            self.listalivros.addItem(item)

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(410, 300, 210, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 60, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 60, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(410, 330, 90, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 60, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 60, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.campopesquisa = QtWidgets.QLineEdit(self)
        self.campopesquisa.setGeometry(QtCore.QRect(140, 31, 220, 28))
        self.campopesquisa.setObjectName("campopesquisa")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(20, 30, 110, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 60, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 60, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.anolancamento = QtWidgets.QLabel(self)
        self.anolancamento.setGeometry(QtCore.QRect(620, 300, 80, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 60, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 60, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 60, 127, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 60, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 60, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 60, 127, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.anolancamento.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.anolancamento.setFont(font)
        self.anolancamento.setText("")
        self.anolancamento.setObjectName("anolancamento")
        self.autor = QtWidgets.QLabel(self)
        self.autor.setGeometry(QtCore.QRect(505, 330, 200, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(6, 60, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 60, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.autor.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(12)
        self.autor.setFont(font)
        self.autor.setText("")
        self.autor.setObjectName("autor")
        self.bpesquisar = QtWidgets.QPushButton(self)
        self.bpesquisar.setGeometry(QtCore.QRect(360, 30, 30, 30))
        self.bpesquisar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bpesquisar.setIcon(icon1)
        self.bpesquisar.setObjectName("bpesquisar")
        self.balugar = QtWidgets.QPushButton(self)
        self.balugar.setGeometry(QtCore.QRect(490, 370, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        self.balugar.setFont(font)
        self.balugar.setObjectName("balugar")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.listalivros.itemClicked.connect(self.show_book)
        self.bpesquisar.clicked.connect(self.search)
        self.balugar.clicked.connect(self.borrow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Buscar", "Buscar"))
        __sortingEnabled = self.listalivros.isSortingEnabled()
        self.listalivros.setSortingEnabled(False)

        for book_index in range(len(books)):
            item = self.listalivros.item(book_index)
            item.setText(_translate("Buscar", books[book_index][0]))

        self.listalivros.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Buscar", "Ano de Lançamento:"))
        self.label_3.setText(_translate("Buscar", "Autor(a):"))
        self.label_4.setText(_translate("Buscar", "Pesquisar"))
        self.balugar.setText(_translate("Buscar", "Alugar"))

    def show_book(self):
        item = self.listalivros.currentItem()
        index = self.listalivros.indexFromItem(item).row()

        self.anolancamento.setText(books[index][1])
        self.autor.setText(books[index][2])
        self.imagemlivro.setPixmap(QtGui.QPixmap("resources/books/"+books[index][4]))

        global clicked_book
        clicked_book = books[index]

    
    def search(self):
        global books
        books = search_books(self.campopesquisa.text())
        self.listalivros.clear()
        for book in books:
            item = QtWidgets.QListWidgetItem()
            self.listalivros.addItem(item)

        self.retranslateUi()

    def borrow(self):
        if clicked_book != []:
            borrow_book(clicked_book)
        else: pass
