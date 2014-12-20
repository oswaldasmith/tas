__author__ = 'Oswald A Smith'
__title__ = 'logindialog'
__version__ = '1.0'
__license__ = 'MIT'
__copyright__ = '2014 Oswald A Smith'

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ui_LoginDialogWindow import Ui_LoginDialogWindow

class LoginDialog(QDialog, Ui_LoginDialogWindow):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)


