from PyQt5.QtWidgets import *
from tcGüncelle_python import Ui_Form_Tc

class Tc(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.tc=Ui_Form_Tc()
        self.tc.setupUi(self)
        self.tc.pushButton_devamet.clicked.connect(self.devam)
        
    def devam(self):
        isim = self.tc.lineEdit_tcDegisiceksim.text()
        sinif = self.tc.lineEdit_sinifbilgi.text()
        tc = self.tc.lineEdit_yenitc.text()

        with open("öğrenciBilgileri.txt", "r") as dosya:
            lines = dosya.readlines()

        with open("öğrenciBilgileri.txt", "w") as dosya:
            for line in lines:
                if "İsim: {}".format(isim) in line:
                    dosya.write("İsim: {}, TC: {}, Sınıf: {}\n".format(isim, tc, sinif))
                else:
                    dosya.write(line)
        print("Öğrenci TC kimlik numarası güncellendi.")

