from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import requests


class Frame(QWidget):
    def __init__(self):
        super().__init__()
        super().setFixedSize(350, 100)
        self.url = "http://data.fixer.io/api/latest?access_key=598e0aff49c69308d4dea62b4b96409d"
        self.response = requests.get(self.url)
        self.json_verisi = self.response.json()
        self.init_gui()

    def init_gui(self):
        para_birimleri = ["TRY", "USD", "EUR", "GBP", "JPY"]
        self.miktarYazi = QLabel("Miktar : ")
        self.neyden = QLabel("Neyden : ")
        self.neye = QLabel("Neye : ")
        self.miktar = QLineEdit()
        self.comboBox_ilkKur = QComboBox()
        self.comboBox_ilkKur.addItems(para_birimleri)
        self.comboBox_ilkKur.setFixedSize(100, 20)
        self.comboBox_sonKur = QComboBox()
        self.comboBox_sonKur.addItems(para_birimleri)
        self.comboBox_sonKur.setFixedSize(100, 20)
        self.hesapla = QPushButton("Hesapla")
        self.hesapla.setFixedSize(100, 40)
        self.hesapla.setIcon(
            QtGui.QIcon("C:\\Users\\ali_e\\Desktop\\Workspaces\\Python Workspace\\Döviz Uygulaması\\iconForButton.png"))
        self.sonuc = QLabel("Sonuç : ")
        v_box = QVBoxLayout()
        h1_box = QHBoxLayout()
        h2_box = QHBoxLayout()
        h1_box.addWidget(self.neyden)
        h1_box.addWidget(self.comboBox_ilkKur)
        h1_box.addStretch()
        h1_box.addWidget(self.neye)
        h1_box.addWidget(self.comboBox_sonKur)
        h2_box.addWidget(self.miktarYazi)
        h2_box.addWidget(self.miktar)
        v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)
        h2_box.addWidget(self.hesapla)
        self.setLayout(v_box)
        self.hesapla.clicked.connect(lambda: self.kurCevir(para_birimleri[self.comboBox_ilkKur.currentIndex()], para_birimleri[self.comboBox_sonKur.currentIndex()], self.miktar.text()))

    def kurCevir(self, neyden, neye, miktar):
        messageBox = QMessageBox(self)
        try:
            miktar = float(miktar)
            if neyden == neye:
                messageBox.setWindowTitle("Sonuç")
                messageBox.setWindowIcon(QtGui.QIcon(
                    "C:\\Users\\ali_e\\Desktop\\Workspaces\\Python Workspace\\Döviz Uygulaması\\iconForButton.png"))
                messageBox.setIcon(QMessageBox.Information)
                messageBox.setText("{} {} = {} {}".format(miktar, neyden, round(miktar, 3), neye))
                messageBox.show()
            else:
                birinci = float(self.json_verisi["rates"][neyden])
                ikinci = float(self.json_verisi["rates"][neye])
                messageBox.setWindowTitle("Sonuç")
                messageBox.setWindowIcon(QtGui.QIcon(
                    "C:\\Users\\ali_e\\Desktop\\Workspaces\\Python Workspace\\Döviz Uygulaması\\iconForButton.png"))
                messageBox.setIcon(QMessageBox.Information)
                messageBox.setText("{} {} = {} {}".format(miktar, neyden, round((miktar/birinci)*ikinci, 3), neye))
                messageBox.show()
        except:
            messageBox.setWindowTitle("Hata")
            messageBox.setWindowIcon(QtGui.QIcon("C:\\Users\\ali_e\\Desktop\\Workspaces\\Python Workspace\\Döviz Uygulaması\\iconForWarning(kucuk).png"))
            messageBox.setIcon(QMessageBox.Warning)
            messageBox.setText("Lütfen miktar için sayı değeri giriniz !")
            messageBox.show()

        finally:
            self.miktar.clear()

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        super().setWindowIcon(
            QtGui.QIcon("C:\\Users\\ali_e\\Desktop\\Workspaces\\Python Workspace\\Döviz Uygulaması\\iconForButton.png"))
        self.frame = Frame()
        self.setCentralWidget(self.frame)
        self.setWindowTitle("Döviz Uygulaması")
        self.show()



