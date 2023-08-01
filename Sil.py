from PyQt5.QtWidgets import *
from SilSayfası_python import Ui_Form_silme

class Sil(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.sil=Ui_Form_silme()
        self.sil.setupUi(self)
        self.sil.pushButton_silSil.clicked.connect(self.ogrenci_sil)
    def ogrenci_sil(self):
        tc = self.sil.lineEdit_siltc.text()
        with open("öğrenciBilgileri.txt", "r") as dosya:
             satirlar = dosya.readlines()

        with open("öğrenciBilgileri.txt", "w") as dosya: # dosya içini yeniden yazar
             for satir in satirlar:
                if "TC: {}".format(tc) not in satir:
                  dosya.write(satir) #satırları yeniden yazmış oluyoruz

        print("Öğrenci bilgileri başarıyla silindi.")