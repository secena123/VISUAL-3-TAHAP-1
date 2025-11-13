import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class Satuan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load(QFile("satuan.ui"), self)
        self.aksi = crud()
        self.tampilData()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

    def bersih(self):
        self.ui.editID.clear()
        self.ui.editKode.clear()
        self.ui.editNama.clear()

    def simpan(self):
        if not self.ui.editID.text():
            QMessageBox.warning(self, "Eror", "ID Kosong")
            return
        self.aksi.simpanSatuan(self.ui.editID.text(), self.ui.editKode.text(), self.ui.editNama.text())
        self.tampilData()
        self.bersih()

    def ubah(self):
        self.aksi.ubahSatuan(self.ui.editID.text(), self.ui.editKode.text(), self.ui.editNama.text())
        self.tampilData()
        self.bersih()

    def hapus(self):
        self.aksi.hapusSatuan(self.ui.editID.text())
        self.tampilData()
        self.bersih()

    def tampilData(self):
        data = self.aksi.dataSatuan()
        self.ui.tabelSatuan.setRowCount(0)
        for i, row in enumerate(data):
            self.ui.tabelSatuan.insertRow(i)
            self.ui.tabelSatuan.setItem(i, 0, QTableWidgetItem(str(row['id'])))
            self.ui.tabelSatuan.setItem(i, 1, QTableWidgetItem(str(row['kode'])))
            self.ui.tabelSatuan.setItem(i, 2, QTableWidgetItem(str(row['nama'])))
