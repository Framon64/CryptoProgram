import sys
import time
from datetime import datetime

from plyer import notification
from pybit import usdt_perpetual
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon

from programWindow import Ui_MainWindow


class HandleMessage(QtWidgets.QMainWindow):    
    def __init__(self, *args, **kwds):
        super(HandleMessage, self).__init__()
        self.programWindow = Ui_MainWindow()
        self.programWindow.setupUi(self)
        self.display()
        self.connect()
        #self.addWindowProgram()
        

    def display(self):
        self.programWindow.lineEdit.setPlaceholderText('Пример: btc, eth, doge')

    #Подключение к API
    def connect(self):
        ws_linear = usdt_perpetual.WebSocket(
            test=False,
            ping_interval=3000,
            ping_timeout=2000,
            domain="bybit"
            )

        ws_linear.kline_stream(
            callback=self.handleMessage, 
            symbol='BTCUSDT', 
            interval="1"
            )
        
    def handleMessage(self, message):
        data = message['data'][0]
        open = data["open"]
        symbol = message["topic"][9:]
        close = data['close']
        turnover = '{0:,}'.format(int(float(data['turnover']))).replace(',', '.')
        priceChange = round((close/open-1)*100, 2)

        self.programWindow.lineEdit_2.setText(str(close))
        self.programWindow.lineEdit_3.setText(symbol)
        self.programWindow.lineEdit_4.setText(str(priceChange))
        self.programWindow.lineEdit_5.setText(str(turnover))

        

        
        
        
    #def addWindowProgram(self):
        
        
        


app = QtWidgets.QApplication([])
application = HandleMessage()
application.show()
sys.exit(app.exec())