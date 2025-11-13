# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barang.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_FormBarang(object):
    def setupUi(self, FormBarang):
        if not FormBarang.objectName():
            FormBarang.setObjectName(u"FormBarang")
        FormBarang.resize(800, 700)
        self.formLayoutWidget = QWidget(FormBarang)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 20, 450, 350))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.l1 = QLabel(self.formLayoutWidget)
        self.l1.setObjectName(u"l1")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.l1)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.l2 = QLabel(self.formLayoutWidget)
        self.l2.setObjectName(u"l2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.l2)

        self.editKode = QLineEdit(self.formLayoutWidget)
        self.editKode.setObjectName(u"editKode")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editKode)

        self.l3 = QLabel(self.formLayoutWidget)
        self.l3.setObjectName(u"l3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l3)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.l4 = QLabel(self.formLayoutWidget)
        self.l4.setObjectName(u"l4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.l4)

        self.editKet = QLineEdit(self.formLayoutWidget)
        self.editKet.setObjectName(u"editKet")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editKet)

        self.l5 = QLabel(self.formLayoutWidget)
        self.l5.setObjectName(u"l5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.l5)

        self.editStokAwal = QLineEdit(self.formLayoutWidget)
        self.editStokAwal.setObjectName(u"editStokAwal")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editStokAwal)

        self.l6 = QLabel(self.formLayoutWidget)
        self.l6.setObjectName(u"l6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.l6)

        self.editStok = QLineEdit(self.formLayoutWidget)
        self.editStok.setObjectName(u"editStok")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editStok)

        self.l7 = QLabel(self.formLayoutWidget)
        self.l7.setObjectName(u"l7")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.l7)

        self.editIDSatuan = QLineEdit(self.formLayoutWidget)
        self.editIDSatuan.setObjectName(u"editIDSatuan")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.editIDSatuan)

        self.l8 = QLabel(self.formLayoutWidget)
        self.l8.setObjectName(u"l8")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.l8)

        self.editRek = QLineEdit(self.formLayoutWidget)
        self.editRek.setObjectName(u"editRek")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.editRek)

        self.l9 = QLabel(self.formLayoutWidget)
        self.l9.setObjectName(u"l9")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.l9)

        self.editStatus = QLineEdit(self.formLayoutWidget)
        self.editStatus.setObjectName(u"editStatus")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.editStatus)

        self.l10 = QLabel(self.formLayoutWidget)
        self.l10.setObjectName(u"l10")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.l10)

        self.editAdm = QLineEdit(self.formLayoutWidget)
        self.editAdm.setObjectName(u"editAdm")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.editAdm)

        self.l11 = QLabel(self.formLayoutWidget)
        self.l11.setObjectName(u"l11")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.l11)

        self.editStaf = QLineEdit(self.formLayoutWidget)
        self.editStaf.setObjectName(u"editStaf")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.editStaf)

        self.l12 = QLabel(self.formLayoutWidget)
        self.l12.setObjectName(u"l12")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.LabelRole, self.l12)

        self.editTgl = QLineEdit(self.formLayoutWidget)
        self.editTgl.setObjectName(u"editTgl")

        self.formLayout.setWidget(11, QFormLayout.ItemRole.FieldRole, self.editTgl)

        self.btnSimpan = QPushButton(FormBarang)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 390, 90, 29))
        self.btnHapus = QPushButton(FormBarang)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 390, 90, 29))
        self.btnUbah = QPushButton(FormBarang)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 390, 90, 29))
        self.btnBersih = QPushButton(FormBarang)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(390, 390, 90, 29))
        self.tabelBarang = QTableWidget(FormBarang)
        if (self.tabelBarang.columnCount() < 5):
            self.tabelBarang.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelBarang.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelBarang.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelBarang.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelBarang.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelBarang.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelBarang.setObjectName(u"tabelBarang")
        self.tabelBarang.setGeometry(QRect(50, 440, 700, 250))

        self.retranslateUi(FormBarang)

        QMetaObject.connectSlotsByName(FormBarang)
    # setupUi

    def retranslateUi(self, FormBarang):
        FormBarang.setWindowTitle(QCoreApplication.translate("FormBarang", u"Data Barang", None))
        self.l1.setText(QCoreApplication.translate("FormBarang", u"ID Barang", None))
        self.l2.setText(QCoreApplication.translate("FormBarang", u"Kode", None))
        self.l3.setText(QCoreApplication.translate("FormBarang", u"Nama Barang", None))
        self.l4.setText(QCoreApplication.translate("FormBarang", u"Keterangan", None))
        self.l5.setText(QCoreApplication.translate("FormBarang", u"Stok Awal", None))
        self.l6.setText(QCoreApplication.translate("FormBarang", u"Stok", None))
        self.l7.setText(QCoreApplication.translate("FormBarang", u"ID Satuan", None))
        self.l8.setText(QCoreApplication.translate("FormBarang", u"Rekomendasi", None))
        self.l9.setText(QCoreApplication.translate("FormBarang", u"Status", None))
        self.l10.setText(QCoreApplication.translate("FormBarang", u"Admin View", None))
        self.l11.setText(QCoreApplication.translate("FormBarang", u"Staf View", None))
        self.l12.setText(QCoreApplication.translate("FormBarang", u"Tanggal Update", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormBarang", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("FormBarang", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("FormBarang", u"Ubah", None))
        self.btnBersih.setText(QCoreApplication.translate("FormBarang", u"Bersih", None))
        ___qtablewidgetitem = self.tabelBarang.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormBarang", u"ID", None));
        ___qtablewidgetitem1 = self.tabelBarang.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormBarang", u"Kode", None));
        ___qtablewidgetitem2 = self.tabelBarang.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormBarang", u"Nama", None));
        ___qtablewidgetitem3 = self.tabelBarang.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormBarang", u"Stok", None));
        ___qtablewidgetitem4 = self.tabelBarang.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormBarang", u"Satuan", None));
    # retranslateUi

