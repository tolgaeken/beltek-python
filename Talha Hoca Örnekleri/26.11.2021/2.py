class Isci:
    def __init__(self, id, ad, soyad):
        self.ad = ad
        self.soyad = soyad
        self.id = id
        self.calistigi_fabrika = None

    def __str__(self):
        return f"İşçi: id={self.id}, a={self.ad}, s={self.soyad} y={self.calistigi_fabrika}"

class Fabrika:
    def __init__(self, ad, il):
        self.ad = ad
        self.il = il
        self.calisanlar = []
        self.sirket = None

    def isci_ata(self, isci):
        self.calisanlar.append(isci)
        isci.calistigi_fabrika = self

    def __str__(self):
        return f"Fabrika: a={self.ad} i={self.il} ş={self.sirket.ad}"

class Sirket:
    def __init__(self, ad):
        self.ad = ad
        self.holding = None
        self.genel_mudur = None
        self.fabrikalar = []

    def fabrika_ata(self, fabrika):
        self.fabrikalar.append(fabrika)
        fabrika.sirket = self

    def mudur_ata(self, mudur):
        self.genel_mudur = mudur
        mudur.calistigi_yer = self

    def __str__(self):
        return f"Şirket: a={self.ad} h={self.holding.ad} m={self.mudur.ad}"

class Holding:
    def __init__(self, ad, ulke):
        self.ad = ad
        self.ulke = ulke
        self.sirketler = []
        self.ceo = None

    def ceo_ata(self, ceo):
        self.ceo = ceo
        ceo.calistigi_yer = self

    def sirket_ata(self, sirket):
        self.sirketler.append(sirket)
        sirket.holding = self

    def __str__(self):
        return f"Holding: a={self.ad} c={self.ceo.ad}"

class Mudur:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad
        self.calistigi_yer = None

    def __str__(self):
        return f"Mudur: {self.ad} {self.soyad} {self.calistigi_yer.ad}"


isci1 = Isci(1, "ali", "veli")
isci2 = Isci(2, "mehmet", "gürbüz")
isci3 = Isci(3, "fatma", "gündüz")

fabrika1 = Fabrika("Fabrika1", "Aydın")
fabrika2 = Fabrika("Fabrika2", "Adana")

fabrika1.isci_ata(isci1)
fabrika1.isci_ata(isci2)
fabrika2.isci_ata(isci3)

sirket1 = Sirket("Sirket1")
sirket2 = Sirket("Sirket2")

sirket1.fabrika_ata(fabrika1)
sirket2.fabrika_ata(fabrika2)

holding1 = Holding("Holding1", "Türkiye")
holding2 = Holding("Holding2", "Türkiye")

holding1.sirket_ata(sirket1)
holding2.sirket_ata(sirket2)

mudur1 = Mudur("Ali", "Şimşek")
mudur2 = Mudur("İrem", "Sak")
mudur3 = Mudur("Veli", "Yılmaz")
mudur4 = Mudur("Hasan", "Yıldırım")

sirket1.mudur_ata(mudur1)
sirket2.mudur_ata(mudur2)

holding1.ceo_ata(mudur3)
holding2.ceo_ata(mudur4)

print(holding1.sirketler[0].genel_mudur)
