# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'satuan.ui'
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

class Ui_FormSatuan(object):
    def setupUi(self, FormSatuan):
        if not FormSatuan.objectName():
            FormSatuan.setObjectName(u"FormSatuan")
        FormSatuan.resize(500, 400)
        self.formLayoutWidget = QWidget(FormSatuan)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 20, 400, 100))
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

        self.btnSimpan = QPushButton(FormSatuan)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 140, 90, 29))
        self.btnHapus = QPushButton(FormSatuan)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(170, 140, 90, 29))
        self.btnUbah = QPushButton(FormSatuan)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(280, 140, 90, 29))
        self.btnBersih = QPushButton(FormSatuan)
        self.btnBersih.setObjectName(u"btnBersih")
        self.btnBersih.setGeometry(QRect(390, 140, 90, 29))
        self.tabelSatuan = QTableWidget(FormSatuan)
        if (self.tabelSatuan.columnCount() < 3):
            self.tabelSatuan.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelSatuan.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelSatuan.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelSatuan.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tabelSatuan.setObjectName(u"tabelSatuan")
        self.tabelSatuan.setGeometry(QRect(50, 190, 430, 200))

        self.retranslateUi(FormSatuan)

        QMetaObject.connectSlotsByName(FormSatuan)
    # setupUi

    def retranslateUi(self, FormSatuan):
        FormSatuan.setWindowTitle(QCoreApplication.translate("FormSatuan", u"Data Satuan", None))
        self.l1.setText(QCoreApplication.translate("FormSatuan", u"ID Satuan", None))
        self.l2.setText(QCoreApplication.translate("FormSatuan", u"Kode", None))
        self.l3.setText(QCoreApplication.translate("FormSatuan", u"Nama Satuan", None))
        self.btnSimpan.setText(QCoreApplication.translate("FormSatuan", u"Simpan", None))
        self.btnHapus.setText(QCoreApplication.translate("FormSatuan", u"Hapus", None))
        self.btnUbah.setText(QCoreApplication.translate("FormSatuan", u"Ubah", None))
        self.btnBersih.setText(QCoreApplication.translate("FormSatuan", u"Bersih", None))
        ___qtablewidgetitem = self.tabelSatuan.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormSatuan", u"ID", None));
        ___qtablewidgetitem1 = self.tabelSatuan.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormSatuan", u"Kode", None));
        ___qtablewidgetitem2 = self.tabelSatuan.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormSatuan", u"Nama", None));
    # retranslateUi

