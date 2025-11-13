import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class Barang(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load(QFile("barang.ui"), self)
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
        self.ui.editKet.clear()
        self.ui.editStokAwal.clear()
        self.ui.editStok.clear()
        self.ui.editIDSatuan.clear()
        self.ui.editRek.clear()
        self.ui.editStatus.clear()
        self.ui.editAdm.clear()
        self.ui.editStaf.clear()
        self.ui.editTgl.clear()

    def simpan(self):
        if not self.ui.editID.text():
            QMessageBox.warning(self, "Eror", "ID Kosong")
            return
        self.aksi.simpanBarang(
            self.ui.editID.text(), self.ui.editKode.text(), self.ui.editNama.text(),
            self.ui.editKet.text(), self.ui.editStokAwal.text(), self.ui.editStok.text(),
            self.ui.editIDSatuan.text(), self.ui.editRek.text(), self.ui.editStatus.text(),
            self.ui.editAdm.text(), self.ui.editStaf.text(), self.ui.editTgl.text()
        )
        self.tampilData()
        self.bersih()

    def ubah(self):
        self.aksi.ubahBarang(
            self.ui.editID.text(), self.ui.editKode.text(), self.ui.editNama.text(),
            self.ui.editKet.text(), self.ui.editStokAwal.text(), self.ui.editStok.text(),
            self.ui.editIDSatuan.text(), self.ui.editRek.text(), self.ui.editStatus.text(),
            self.ui.editAdm.text(), self.ui.editStaf.text(), self.ui.editTgl.text()
        )
        self.tampilData()
        self.bersih()

    def hapus(self):
        self.aksi.hapusBarang(self.ui.editID.text())
        self.tampilData()
        self.bersih()

    def tampilData(self):
        data = self.aksi.dataBarang()
        self.ui.tabelBarang.setRowCount(0)
        for i, row in enumerate(data):
            self.ui.tabelBarang.insertRow(i)
            self.ui.tabelBarang.setItem(i, 0, QTableWidgetItem(str(row['id'])))
            self.ui.tabelBarang.setItem(i, 1, QTableWidgetItem(str(row['kode'])))
            self.ui.tabelBarang.setItem(i, 2, QTableWidgetItem(str(row['nama'])))
            self.ui.tabelBarang.setItem(i, 3, QTableWidgetItem(str(row['stok'])))
            self.ui.tabelBarang.setItem(i, 4, QTableWidgetItem(str(row['satuan_id'])))
