import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class Riwayat(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load(QFile("riwayat.ui"), self)
        self.aksi = crud()
        self.tampilData()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

    def bersih(self):
        self.ui.editID.clear()
        self.ui.editIDUser.clear()
        self.ui.editIDBrg.clear()
        self.ui.editJenis.clear()
        self.ui.editQty.clear()
        self.ui.editKet.clear()
        self.ui.editTgl.clear()

    def simpan(self):
        if not self.ui.editID.text():
            QMessageBox.warning(self, "Eror", "ID Kosong")
            return
        self.aksi.simpanRiwayat(
            self.ui.editID.text(), self.ui.editIDUser.text(), self.ui.editIDBrg.text(),
            self.ui.editJenis.text(), self.ui.editQty.text(), self.ui.editKet.text(), self.ui.editTgl.text()
        )
        self.tampilData()
        self.bersih()

    def ubah(self):
        self.aksi.ubahRiwayat(
            self.ui.editID.text(), self.ui.editIDUser.text(), self.ui.editIDBrg.text(),
            self.ui.editJenis.text(), self.ui.editQty.text(), self.ui.editKet.text(), self.ui.editTgl.text()
        )
        self.tampilData()
        self.bersih()

    def hapus(self):
        self.aksi.hapusRiwayat(self.ui.editID.text())
        self.tampilData()
        self.bersih()

    def tampilData(self):
        data = self.aksi.dataRiwayat()
        self.ui.tabelRiwayat.setRowCount(0)
        for i, row in enumerate(data):
            self.ui.tabelRiwayat.insertRow(i)
            self.ui.tabelRiwayat.setItem(i, 0, QTableWidgetItem(str(row['id'])))
            self.ui.tabelRiwayat.setItem(i, 1, QTableWidgetItem(str(row['user_id'])))
            self.ui.tabelRiwayat.setItem(i, 2, QTableWidgetItem(str(row['barang_id'])))
            self.ui.tabelRiwayat.setItem(i, 3, QTableWidgetItem(str(row['jenis'])))
            self.ui.tabelRiwayat.setItem(i, 4, QTableWidgetItem(str(row['qty'])))
