"""
Author : aesavas
Currency Calculation Application - Döviz Hesaplama Uygulaması
This project uses fixer.io free JSON API
"""

from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import requests


class Frame(QWidget):
    def __init__(self):
        super().__init__()
        super().setFixedSize(350, 100)
        self.url = "http://data.fixer.io/api/latest?access_key=598e0aff49c69308d4dea62b4b96409d"
        self.response = requests.get(self.url)
        self.json_data = self.response.json()
        self.init_gui()

    def init_gui(self) :
        currency_units = ["TRY", "USD", "EUR", "GBP", "JPY"]

        # The amount of money entered in the interface.
        self.amountLabel = QLabel("Amount : ")
        self.amount = QLineEdit()

        # Converted currency
        self.fromCurrency = QLabel("From : ")
        self.comboBox_FirstRate = QComboBox()
        self.comboBox_FirstRate.addItems(currency_units)
        self.comboBox_FirstRate.setFixedSize(100, 20)

        # Which currency unit to convert
        self.toCurrency = QLabel("To : ")
        self.comboBox_LastRate = QComboBox()
        self.comboBox_LastRate.addItems(currency_units)
        self.comboBox_LastRate.setFixedSize(100, 20)

        # Button to calculate
        self.calculate = QPushButton("Hesapla")
        self.calculate.setFixedSize(100, 40)
        self.calculate.setIcon(QtGui.QIcon("icons\\iconForButton.png"))

        # Layout plan
        v_box = QVBoxLayout()
        h1_box = QHBoxLayout()
        h2_box = QHBoxLayout()
        h1_box.addWidget(self.fromCurrency)
        h1_box.addWidget(self.comboBox_FirstRate)
        h1_box.addStretch()
        h1_box.addWidget(self.toCurrency)
        h1_box.addWidget(self.comboBox_LastRate)
        h2_box.addWidget(self.amountLabel)
        h2_box.addWidget(self.amount)
        v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)
        h2_box.addWidget(self.calculate)
        self.setLayout(v_box)

        # Button function
        self.calculate.clicked.connect(lambda: self.kurCevir(currency_units[self.comboBox_FirstRate.currentIndex()],
                                                             currency_units[self.comboBox_LastRate.currentIndex()],
                                                             self.amount.text()))

    """
        We need these parameters because we use free API. This situation creates some limitation.
        We can not convert directly. Firstly we convert EURO then convert to desired unit.
        @param first : The value of the unit to be converted in EURO.
        @param second : The value of the target unit in EURO.
    """
    def kurCevir(self, fromCurrency, toCurrency, amount):
        messageBox = QMessageBox(self)
        try:
            amount = float(amount)
            if fromCurrency == toCurrency:
                messageBox.setWindowTitle("Result")
                messageBox.setWindowIcon(QtGui.QIcon("icons\\iconForButton.png"))
                messageBox.setIcon(QMessageBox.Information)
                messageBox.setText("{} {} = {} {}".format(amount, fromCurrency, round(amount, 3), toCurrency))
                messageBox.show()
            else:
                first = float(self.json_data["rates"][fromCurrency])  # The value of To be converted currency
                second = float(self.json_data["rates"][toCurrency])   # The value of Target currency
                messageBox.setWindowTitle("Result")
                messageBox.setWindowIcon(QtGui.QIcon("icons\\iconForButton.png"))
                messageBox.setIcon(QMessageBox.Information)
                messageBox.setText("{} {} = {} {}".format(amount, fromCurrency, round((amount / first) * second, 3), toCurrency))
                messageBox.show()
        except:
            messageBox.setWindowTitle("Warning")
            messageBox.setWindowIcon(QtGui.QIcon("icons\\iconForWarning(kucuk).png"))
            messageBox.setIcon(QMessageBox.Warning)
            messageBox.setText("Please enter the number value for the quantity!")
            messageBox.show()

        finally:
            self.amount.clear()


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        super().setWindowIcon(
            QtGui.QIcon("icons\\iconForButton.png"))
        self.frame = Frame()
        self.setCentralWidget(self.frame)
        self.setWindowTitle("Currency Application")
        self.show()



