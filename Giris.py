from PyQt5.QtWidgets import *
from Giris_python import Ui_Form_Giris
from EkleSayfası import Ekle
from Sil import Sil
from tcGüncelle import Tc
from BilgiGüncelleme import BilgiGuncelle

class Giris(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.giris=Ui_Form_Giris()
        self.giris.setupUi(self)
        self.ekle=Ekle()
        self.sil=Sil()
        self.tc=Tc()
        self.guncelle=BilgiGuncelle()
        self.giris.pushButton_guncelle.clicked.connect(self.ogrenci_guncelle_git)
        self.giris.pushButton_ekle.clicked.connect(self.ogrenci_ekle_git)
        self.giris.pushButton_sil.clicked.connect(self.ogrenci_sil_git)
        self.giris.pushButton_goruntule.clicked.connect(self.ogrenci_goruntule_git)
        
    def ogrenci_guncelle_git(self):
        self.hide()
        self.guncelle.show()


    def ogrenci_goruntule_git(self):
        with open("öğrenciBilgileri.txt","r") as dosya:
            lines=dosya.readlines()
            print("Kayıtlı Öğrenci Bilgileri Gösteriliyor...")
            print("------------------------------------------")
            for line in lines:
                print(line)


    def ogrenci_ekle_git(self):
        self.hide()
        self.ekle.show()

    def ogrenci_sil_git(self):
        self.hide()
        self.sil.show()
        
app=QApplication([])
pencere=Giris()
pencere.show()
app.exec_()


