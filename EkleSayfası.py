from PyQt5.QtWidgets import *
from EkleSayfası_python import Ui_Form_ekle

class Ekle(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.ekle=Ui_Form_ekle()
        self.ekle.setupUi(self)
        self.ekle.pushButton_ekleEkle.clicked.connect(self.ogrenci_ekle)
    def ogrenci_ekle(self):
        tc=self.ekle.lineEdit_tc.text()
        isim=self.ekle.lineEdit_isim.text()
        sinif=self.ekle.lineEdit_sinif.text()
        with open("öğrenciBilgileri.txt","a") as dosya :
            dosya.write("İsim: {}, TC: {}, Sınıf: {}\n".format(isim, tc, sinif))
        print("Öğrenci bilgileri başarıyla eklendi")