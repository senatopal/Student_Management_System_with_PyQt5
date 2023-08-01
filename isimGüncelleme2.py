from PyQt5.QtWidgets import *
from İsimGüncelleme2_python import Ui_Form_isimGuncelle2

class İsimGüncelle(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.guncelle=Ui_Form_isimGuncelle2()
        self.guncelle.setupUi(self)
        self.guncelle.pushButton_isimSinifGuncelle.clicked.connect(self.Guncelle)
    def Guncelle(self):
        tc=self.guncelle.lineEdit.text()
        isim=self.guncelle.lineEdit_isimGuncelle.text()
        sinif=self.guncelle.lineEdit_sinifGuncelle.text()
        with open("öğrenciBilgileri.txt","r") as dosya:
            lines=dosya.readlines()
        with open("öğrenciBilgileri.txt","w") as dosya:
            for line in lines:
                if "TC: {}".format(tc) in line:
                    dosya.write("İsim: {}, TC: {}, Sınıf: {}\n".format(isim, tc, sinif))
                else:
                    dosya.write(line)
        print("Öğrenci bilgileri güncellendi.")