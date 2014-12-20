__author__ = 'Oswald A Smith'
__title__ = 'tas'
__version__ = '1.0'
__license__ = 'MIT'
__copyright__ = '2014 Oswald A Smith'


import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from logindialog import LoginDialog
from mainwindow import MainWindow





if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_dialog = LoginDialog()
    login_dialog.show()

    main_window = MainWindow()
    main_window.show()
    app.exec_()
