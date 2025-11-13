# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from barang import Barang
from pesanan import Pesanan
from riwayat import Riwayat
from satuan import Satuan

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load(QFile("main.ui"), self)

        self.ui.actionBarang.triggered.connect(self.buka_barang)
        self.ui.actionPesanan.triggered.connect(self.buka_pesanan)
        self.ui.actionRiwayat.triggered.connect(self.buka_riwayat)
        self.ui.actionSatuan.triggered.connect(self.buka_satuan)

    def buka_barang(self):
        self.window_barang = Barang()
        self.window_barang.show()

    def buka_pesanan(self):
        self.window_pesanan = Pesanan()
        self.window_pesanan.show()

    def buka_riwayat(self):
        self.window_riwayat = Riwayat()
        self.window_riwayat.show()

    def buka_satuan(self):
        self.window_satuan = Satuan()
        self.window_satuan.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.ui.show()
    sys.exit(app.exec())
