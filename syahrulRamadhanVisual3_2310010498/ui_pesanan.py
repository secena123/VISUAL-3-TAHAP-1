# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pesanan.ui'
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

class Ui_FormPesanan(object):
    def setupUi(self, FormPesanan):
        if not FormPesanan.objectName():
            FormPesanan.setObjectName(u"FormPesanan")
        FormPesanan.resize(750, 600)
        self.formLayoutWidget = QWidget(FormPesanan)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 20, 450, 320))
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

        self.editIDMkt = QLineEdit(self.formLayoutWidget)
        self.editIDMkt.setObjectName(u"editIDMkt")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editIDMkt)

        self.l3 = QLabel(self.formLayoutWidget)
        self.l3.setObjectName(u"l3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l3)

        self.editIDStaf = QLineEdit(self.formLayoutWidget)
        self.editIDStaf.setObjectName(u"editIDStaf")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editIDStaf)

        self.l4 = QLabel(self.formLayoutWidget)
        self.l4.setObjectName(u"l4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.l4)

        self.editIDBrg = QLineEdit(self.formLayoutWidget)
        self.editIDBrg.setObjectName(u"editIDBrg")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editIDBrg)

        self.l5 = QLabel(self.formLayoutWidget)
        self.l5.setObjectName(u"l5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.l5)

        self.editMinta = QLineEdit(self.formLayoutWidget)
        self.editMinta.setObjectName(u"editMinta")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editMinta)

        self.l6 = QLabel(self.formLayoutWidget)
        self.l6.setObjectName(u"l6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.l6)

        self.editKirim = QLineEdit(self.formLayoutWidget)
        self.editKirim.setObjectName(u"editKirim")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editKirim)

        self.l7 = QLabel(self.formLayoutWidget)
        self.l7.setObjectName(u"l7")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.l7)

        self.editTglMinta = QLineEdit(self.formLayoutWidget)
        self.editTglMinta.setObjectName(u"editTglMinta")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.editTglMinta)

        self.l8 = QLabel(self.formLayoutWidget)
        self.l8.setObjectName(u"l8")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.l8)

        self.editTglKirim = QLineEdit(self.formLayoutWidget)
        self.editTglKirim.setObjectName(u"editTglKirim")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.editTglKirim)

        self.l9 = QLabel(self.formLayoutWidget)
        self.l9.setObjectName(u"l9")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.l9)

        self.editStatus = QLineEdit(self.formLayoutWidget)
        self.editStatus.setObjectName(u"editStatus")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.editStatus)

        self.l10 = QLabel(self.formLayoutWidget)
        self.l10.setObjectName(u"l10")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.l10)

        self.editRek = QLineEdit(self.formLayoutWidget)
        self.editRek.setObjectName(u"editRek")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.editRek)

        self.l11 = QLabel(self.formLayoutWidget)
        self.l11.setObjectName(u"l11")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.l11)

        self.editStatRek = QLineEdit(self.formLayoutWidget)
        self.editStatRek.setObjectName(u"editStatRek")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.FieldRole, self.editStatRek)

        self.btnSimpan = QPushButton(FormPesanan)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 350, 90, 29))
        self.btnHapus = QPushButton(FormPesanan)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 350, 90, 29))
        self.btnUbah = QPushButton(FormPesanan)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 350, 90, 29))
        self.btnBersih = QPushButton(FormPesanan)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(390, 350, 90, 29))
        self.tabelPesanan = QTableWidget(FormPesanan)
        if (self.tabelPesanan.columnCount() < 5):
            self.tabelPesanan.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelPesanan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelPesanan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelPesanan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelPesanan.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelPesanan.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelPesanan.setObjectName(u"tabelPesanan")
        self.tabelPesanan.setGeometry(QRect(50, 400, 650, 180))

        self.retranslateUi(FormPesanan)

        QMetaObject.connectSlotsByName(FormPesanan)
    # setupUi

    def retranslateUi(self, FormPesanan):
        FormPesanan.setWindowTitle(QCoreApplication.translate("FormPesanan", u"Data Pesanan", None))
        self.l1.setText(QCoreApplication.translate("FormPesanan", u"ID Pesanan", None))
        self.l2.setText(QCoreApplication.translate("FormPesanan", u"ID Marketing", None))
        self.l3.setText(QCoreApplication.translate("FormPesanan", u"ID Staf", None))
        self.l4.setText(QCoreApplication.translate("FormPesanan", u"ID Barang", None))
        self.l5.setText(QCoreApplication.translate("FormPesanan", u"Permintaan", None))
        self.l6.setText(QCoreApplication.translate("FormPesanan", u"Pengiriman", None))
        self.l7.setText(QCoreApplication.translate("FormPesanan", u"Tgl Minta", None))
        self.l8.setText(QCoreApplication.translate("FormPesanan", u"Tgl Kirim", None))
        self.l9.setText(QCoreApplication.translate("FormPesanan", u"Status", None))
        self.l10.setText(QCoreApplication.translate("FormPesanan", u"Rekomendasi", None))
        self.l11.setText(QCoreApplication.translate("FormPesanan", u"Status Rek", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormPesanan", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("FormPesanan", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("FormPesanan", u"Ubah", None))
        self.btnBersih.setText(QCoreApplication.translate("FormPesanan", u"Bersih", None))
        ___qtablewidgetitem = self.tabelPesanan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormPesanan", u"ID", None));
        ___qtablewidgetitem1 = self.tabelPesanan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormPesanan", u"Barang", None));
        ___qtablewidgetitem2 = self.tabelPesanan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormPesanan", u"Minta", None));
        ___qtablewidgetitem3 = self.tabelPesanan.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormPesanan", u"Kirim", None));
        ___qtablewidgetitem4 = self.tabelPesanan.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormPesanan", u"Status", None));
    # retranslateUi

