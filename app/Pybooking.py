# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functions import signup, call_screen
from login import Ui_Login
from splash import Ui_Splash

import random
import time


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QDialog()
    ui = Ui_Splash()
    ui.setupUi(splash)
    splash.show()

    movie = QtGui.QMovie("resources/loading_book.gif")
    ui.livro.setMovie(movie)
    movie.start()

    for i in range(0, 101):
        ui.barraprogresso.setValue(i)
        time.sleep(float("0.0" + str(random.randint(3,7))))
        app.processEvents()

    call_screen(splash, Ui_Login())

    sys.exit(app.exec_())
