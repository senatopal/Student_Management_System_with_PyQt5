# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Giris.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Giris(object):
    def setupUi(self, Form_Giris):
        Form_Giris.setObjectName("Form_Giris")
        Form_Giris.resize(400, 488)
        self.label = QtWidgets.QLabel(Form_Giris)
        self.label.setGeometry(QtCore.QRect(20, 30, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form_Giris)
        self.label_2.setGeometry(QtCore.QRect(0, 110, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName("label_2")
        self.pushButton_ekle = QtWidgets.QPushButton(Form_Giris)
        self.pushButton_ekle.setGeometry(QtCore.QRect(0, 150, 131, 41))
        self.pushButton_ekle.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_ekle.setObjectName("pushButton_ekle")
        self.pushButton_sil = QtWidgets.QPushButton(Form_Giris)
        self.pushButton_sil.setGeometry(QtCore.QRect(0, 210, 131, 41))
        self.pushButton_sil.setObjectName("pushButton_sil")
        self.pushButton_goruntule = QtWidgets.QPushButton(Form_Giris)
        self.pushButton_goruntule.setGeometry(QtCore.QRect(0, 270, 131, 51))
        self.pushButton_goruntule.setObjectName("pushButton_goruntule")
        self.pushButton_guncelle = QtWidgets.QPushButton(Form_Giris)
        self.pushButton_guncelle.setGeometry(QtCore.QRect(0, 340, 131, 51))
        self.pushButton_guncelle.setObjectName("pushButton_guncelle")

        self.retranslateUi(Form_Giris)
        QtCore.QMetaObject.connectSlotsByName(Form_Giris)

    def retranslateUi(self, Form_Giris):
        _translate = QtCore.QCoreApplication.translate
        Form_Giris.setWindowTitle(_translate("Form_Giris", "Form"))
        self.label.setText(_translate("Form_Giris", "ÖĞRENCİ YÖNETİM SİSTEMİNE HOŞ GELDİNİZ"))
        self.label_2.setText(_translate("Form_Giris", "Yapmak İstediğiniz İşlemi Seçiniz"))
        self.pushButton_ekle.setText(_translate("Form_Giris", "Öğrenci Ekle"))
        self.pushButton_sil.setText(_translate("Form_Giris", "Öğrenci Sil"))
        self.pushButton_goruntule.setText(_translate("Form_Giris", "Öğrencileri Görüntüle"))
        self.pushButton_guncelle.setText(_translate("Form_Giris", "Öğrenci Bilgi Güncelle"))
