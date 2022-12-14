import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from programWindow import Ui_MainWindow
import time
from datetime import datetime
from pybit import usdt_perpetual
from plyer import notification

class HandleMessage(QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwds):
        super(HandleMessage, self).__init__()
        self.programWindow = Ui_MainWindow()
        self.programWindow.setupUi(self)
        self.display()

    def display(self):
        self.programWindow.lineEdit.setPlaceholderText('Пример: btc, eth, doge')




app = QtWidgets.QApplication([])
application = HandleMessage()
application.show()
sys.exit(app.exec())