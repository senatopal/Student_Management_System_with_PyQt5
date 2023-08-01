from PyQt5.QtWidgets import *
from BilgiGüncelleme_python import Ui_Form_guncelle
from tcGüncelle import Tc
from isimGüncelleme2 import İsimGüncelle

class BilgiGuncelle(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.bilgi=Ui_Form_guncelle()
        self.bilgi.setupUi(self)
        self.tc=Tc()
        self.guncelle=İsimGüncelle()
        self.bilgi.radioButton_tc.toggled.connect(self.ogrenci_tc_duzenleme_git)
        self.bilgi.radioButton_isim.toggled.connect(self.ogrenci_isim_sinif_duzenleme_git)

    def ogrenci_isim_sinif_duzenleme_git(self):
        self.hide()
        self.guncelle.show()

    def ogrenci_tc_duzenleme_git(self):
        self.hide()
        self.tc.show()
        