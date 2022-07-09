class Insan:
    def __init__(self, ad, soyad, cinsiyet):
        self.ad = ad
        self.soyad = soyad
        self.cinsiyet = cinsiyet
        self.TCKN = None
        self.kan_grubu = None


class IsYeri:
    def __init__(self, ad):
        self.ad = ad
        self.servis = False
        self.calisanlar = []
        self.adres = ""


class Isci(Insan):
    def __init__(self, ad, soyad, cinsiyet, uzmanlik):
        super().__init__(ad, soyad, cinsiyet)
        self.uzmanlik = uzmanlik
        self.diploma = None
        self.kidem = 0
        self.fabrika = None


class GenelMudur(Insan):
    def __init__(self, ad, soyad, cinsiyet):
        super().__init__(ad, soyad, cinsiyet)
        self.kidem = 0
        self.sirket = None
        self.diploma = None


class CEO(Insan):
    def __init__(self, ad, soyad, cinsiyet):
        super().__init__(ad, soyad, cinsiyet)
        self.kidem = 0
        self.diploma = None
        self.holding = None


class Holding(IsYeri):
    def __init__(self, ad, sicil):
        super().__init__(ad)
        self.ticari_sicil = sicil
        self.yonetim_kurulu = []
        self.sirket_yetki = False
        self.ceo = None

    def ceo_ata(self, ceo):
        self.ceo = ceo
        ceo.holding = self


class Sirket(IsYeri):
    def __init__(self, ad, sicil):
        super().__init__(ad)
        self.ticari_sicil = sicil
        self.fabrika_yetki = False
        self.genel_mudur = False
    

    def mudur_ata(self, mudur):
        self.genel_mudur = mudur
        mudur.sirket = self


class Fabrika(IsYeri):
    def __init__(self, ad, alan):
        super().__init__(ad)
        self.alan = alan
        self.sertifikalar = []
        self.atolyeler = []
        self.makineler = []


    def isci_ata(self, isci):
        self.calisanlar.append(isci)
        isci.fabrika = self


fabrika1 = Fabrika("Bisküvi Fabrikası", 800)
mudur1 = GenelMudur("Murat", "Kuşçu", "Erkek")
sirket1 = Sirket("Bisküviler", 2131231421)
print(mudur1.sirket)
sirket1.mudur_ata(mudur1)
print(mudur1.sirket.ad)