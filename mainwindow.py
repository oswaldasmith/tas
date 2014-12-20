__author__ = 'Oswald A Smith'
__title__ = 'mainwindow'
__version__ = '1.0'
__license__ = 'MIT'
__copyright__ = '2014 Oswald A Smith'

from PyQt5.QtWidgets import *
from ui_MainWindow import Ui_MainWindow
from logindialog import LoginDialog

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.actionNew_Tournament.triggered.connect(self.login)

    def new_tournament(self):
        msgBox = QMessageBox(self)
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setWindowTitle("Pythonthusiast")
        msgBox.setText("Are you sure you want to quit?")
        msgBox.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        msgBox.setDefaultButton(QMessageBox.Yes)
        msgBox.exec_()

    def login(self):
        dialog = LoginDialog()
        dialog.show()