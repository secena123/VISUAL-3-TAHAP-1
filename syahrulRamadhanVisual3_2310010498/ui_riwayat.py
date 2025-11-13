# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'riwayat.ui'
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

class Ui_FormRiwayat(object):
    def setupUi(self, FormRiwayat):
        if not FormRiwayat.objectName():
            FormRiwayat.setObjectName(u"FormRiwayat")
        FormRiwayat.resize(600, 500)
        self.formLayoutWidget = QWidget(FormRiwayat)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 20, 450, 210))
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

        self.editIDUser = QLineEdit(self.formLayoutWidget)
        self.editIDUser.setObjectName(u"editIDUser")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editIDUser)

        self.l3 = QLabel(self.formLayoutWidget)
        self.l3.setObjectName(u"l3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.l3)

        self.editIDBrg = QLineEdit(self.formLayoutWidget)
        self.editIDBrg.setObjectName(u"editIDBrg")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editIDBrg)

        self.l4 = QLabel(self.formLayoutWidget)
        self.l4.setObjectName(u"l4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.l4)

        self.editJenis = QLineEdit(self.formLayoutWidget)
        self.editJenis.setObjectName(u"editJenis")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editJenis)

        self.l5 = QLabel(self.formLayoutWidget)
        self.l5.setObjectName(u"l5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.l5)

        self.editQty = QLineEdit(self.formLayoutWidget)
        self.editQty.setObjectName(u"editQty")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editQty)

        self.l6 = QLabel(self.formLayoutWidget)
        self.l6.setObjectName(u"l6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.l6)

        self.editKet = QLineEdit(self.formLayoutWidget)
        self.editKet.setObjectName(u"editKet")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editKet)

        self.l7 = QLabel(self.formLayoutWidget)
        self.l7.setObjectName(u"l7")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.l7)

        self.editTgl = QLineEdit(self.formLayoutWidget)
        self.editTgl.setObjectName(u"editTgl")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.editTgl)

        self.btnSimpan = QPushButton(FormRiwayat)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 250, 90, 29))
        self.btnHapus = QPushButton(FormRiwayat)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 250, 90, 29))
        self.btnUbah = QPushButton(FormRiwayat)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 250, 90, 29))
        self.btnBersih = QPushButton(FormRiwayat)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(390, 250, 90, 29))
        self.tabelRiwayat = QTableWidget(FormRiwayat)
        if (self.tabelRiwayat.columnCount() < 5):
            self.tabelRiwayat.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelRiwayat.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelRiwayat.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelRiwayat.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelRiwayat.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelRiwayat.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelRiwayat.setObjectName(u"tabelRiwayat")
        self.tabelRiwayat.setGeometry(QRect(50, 300, 500, 180))

        self.retranslateUi(FormRiwayat)

        QMetaObject.connectSlotsByName(FormRiwayat)
    # setupUi

    def retranslateUi(self, FormRiwayat):
        FormRiwayat.setWindowTitle(QCoreApplication.translate("FormRiwayat", u"Data Riwayat", None))
        self.l1.setText(QCoreApplication.translate("FormRiwayat", u"ID Riwayat", None))
        self.l2.setText(QCoreApplication.translate("FormRiwayat", u"ID User", None))
        self.l3.setText(QCoreApplication.translate("FormRiwayat", u"ID Barang", None))
        self.l4.setText(QCoreApplication.translate("FormRiwayat", u"Jenis", None))
        self.l5.setText(QCoreApplication.translate("FormRiwayat", u"Qty", None))
        self.l6.setText(QCoreApplication.translate("FormRiwayat", u"Keterangan", None))
        self.l7.setText(QCoreApplication.translate("FormRiwayat", u"Tanggal", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormRiwayat", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("FormRiwayat", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("FormRiwayat", u"Ubah", None))
        self.btnBersih.setText(QCoreApplication.translate("FormRiwayat", u"Bersih", None))
        ___qtablewidgetitem = self.tabelRiwayat.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormRiwayat", u"ID", None));
        ___qtablewidgetitem1 = self.tabelRiwayat.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormRiwayat", u"User", None));
        ___qtablewidgetitem2 = self.tabelRiwayat.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormRiwayat", u"Barang", None));
        ___qtablewidgetitem3 = self.tabelRiwayat.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormRiwayat", u"Jenis", None));
        ___qtablewidgetitem4 = self.tabelRiwayat.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormRiwayat", u"Qty", None));
    # retranslateUi

