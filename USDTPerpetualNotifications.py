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
        self.connect()

    def display(self):
        self.programWindow.lineEdit.setPlaceholderText('Пример: btc, eth, doge')

    def connect(self):

        ws_linear = usdt_perpetual.WebSocket(
            test=False,
            ping_interval=3000,
            ping_timeout=2000,
            domain="bybit"
            )

        ws_linear.kline_stream(
            callback=self.handle_message, 
            symbol='BTCUSDT', 
            interval="1"
            )

    def handle_message(self, msg):
        data = msg['data'][0]
        close = data["close"]
        print(f"Цена закрытия: {close}")



app = QtWidgets.QApplication([])
application = HandleMessage()
application.show()
sys.exit(app.exec())