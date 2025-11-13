import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud

class Pesanan(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load(QFile("pesanan.ui"), self)
        self.aksi = crud()
        self.tampilData()
        self.ui.btnSimpan.clicked.connect(self.simpan)
        self.ui.btnUbah.clicked.connect(self.ubah)
        self.ui.btnHapus.clicked.connect(self.hapus)
        self.ui.btnBersih.clicked.connect(self.bersih)

    def bersih(self):
        self.ui.editID.clear()
        self.ui.editIDMkt.clear()
        self.ui.editIDStaf.clear()
        self.ui.editIDBrg.clear()
        self.ui.editMinta.clear()
        self.ui.editKirim.clear()
        self.ui.editTglMinta.clear()
        self.ui.editTglKirim.clear()
        self.ui.editStatus.clear()
        self.ui.editRek.clear()
        self.ui.editStatRek.clear()

    def simpan(self):
        if not self.ui.editID.text():
            QMessageBox.warning(self, "Eror", "ID Kosong")
            return
        self.aksi.simpanPesanan(
            self.ui.editID.text(), self.ui.editIDMkt.text(), self.ui.editIDStaf.text(),
            self.ui.editIDBrg.text(), self.ui.editMinta.text(), self.ui.editKirim.text(),
            self.ui.editTglMinta.text(), self.ui.editTglKirim.text(), self.ui.editStatus.text(),
            self.ui.editRek.text(), self.ui.editStatRek.text()
        )
        self.tampilData()
        self.bersih()

    def ubah(self):
        self.aksi.ubahPesanan(
            self.ui.editID.text(), self.ui.editIDMkt.text(), self.ui.editIDStaf.text(),
            self.ui.editIDBrg.text(), self.ui.editMinta.text(), self.ui.editKirim.text(),
            self.ui.editTglMinta.text(), self.ui.editTglKirim.text(), self.ui.editStatus.text(),
            self.ui.editRek.text(), self.ui.editStatRek.text()
        )
        self.tampilData()
        self.bersih()

    def hapus(self):
        self.aksi.hapusPesanan(self.ui.editID.text())
        self.tampilData()
        self.bersih()

    def tampilData(self):
        data = self.aksi.dataPesanan()
        self.ui.tabelPesanan.setRowCount(0)
        for i, row in enumerate(data):
            self.ui.tabelPesanan.insertRow(i)
            self.ui.tabelPesanan.setItem(i, 0, QTableWidgetItem(str(row['id'])))
            self.ui.tabelPesanan.setItem(i, 1, QTableWidgetItem(str(row['barang_id'])))
            self.ui.tabelPesanan.setItem(i, 2, QTableWidgetItem(str(row['permintaan'])))
            self.ui.tabelPesanan.setItem(i, 3, QTableWidgetItem(str(row['pengiriman'])))
            self.ui.tabelPesanan.setItem(i, 4, QTableWidgetItem(str(row['status'])))
