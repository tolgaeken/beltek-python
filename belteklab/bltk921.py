class Insan:
    def __init__(self,ad,soyad,cinsiyet):
        self.ad = ad
        self.soyad = soyad
        self.cinsiyet = cinsiyet
        self.tckn = None
        self.kanGrubu = None

class Isyeri:
    def __init__(self,ad):
        self.ad = ad
        self.servis = None
        self.adres = None
        self.calisanlar = []
        

class GenelMudur(Insan):
    def __init__(self,ad,soyad,cinsiyet):
        super().__init__(ad,soyad,cinsiyet)
        self.sirket = None
        self.kidem = None
        self.diploma = None

class Isci(Insan):
    def __init__(self,ad,soyad,cinsiyet,uzmanlik):
        super().__init__(ad,soyad,cinsiyet)
        self.fabrika = None
        self.uzmamlik = uzmanlik
        self.kidem = None
        self.diploma = None


class Ceo(Insan):
    def __init__(self,ad,soyad,cinsiyet):
        super().__init__(ad,soyad,cinsiyet)
        self.holding = None
        self.kidem = None
        self.diploma = None


class Holding(Isyeri):
    def __init__(self,ad,ticariSicilNo):
        super().__init__(ad)
        self.ticariSicilNo = ticariSicilNo
        self.yonetimKurulu = None
        self.sirketYetkisi = None
        self.ceo = None
    
    def ceoAta(self,ceo):
        self.ceo = ceo
        ceo.holding = self


class Sirket(Isyeri):
    def __init__(self,ad,ticariSicilNo):
        super().__init__(ad)
        self.fabrikaYetkisi = None
        self.ticariSicilNo = ticariSicilNo
        self.genelMudur
    
    def genelMudurAta(self,mudur):
        self.genelMudur = mudur
        mudur.sirket = self

class Fabrika(Isyeri):
    def __init__(self,ad,alan):
        super().__init__(ad)
        self.alan = alan
        self.sertifikalar = []
        self.atolyeler = []
        self.makineler = []
        self.isciler = []
    
    def isciAta(self,isci):
        self.isciler.append(isci)
        isci.fabrika = self
    
    def sertifikaAta(self,sertifika):
        self.sertifikalar.append(sertifika)

    def atolyeAta(self,atolye):
        self.atolyeler.append(atolye)
    
    def makineAta(self,makine):
        self.makineler.append(makine)