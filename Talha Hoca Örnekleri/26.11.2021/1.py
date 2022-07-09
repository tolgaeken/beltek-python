class Kedi:
    def __init__(self, ad, cins, yas):
        self.ad = ad
        self.cins = cins
        self.yas = yas
        self.asilar = False
        self.renk = ""
        self.sahip = None

    def __str__(self):
        return f"{self.ad} {self.cins} {self.yas}"

class Kopek:
    def __init__(self, ad, cins, yas):
        self.ad = ad
        self.cins = cins
        self.yas = yas
        self.asilar = False
        self.renk = ""
        self.sahip = None

    def __str__(self):
        return f"{self.ad} {self.cins} {self.yas}"

class Insan:
    def __init__(self, ad, soyad, yas, id):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.id = id
        self.meslek = ""
        self.kan_grubu = ""
        self.evcil_hayvanlar = []

    def sahiplen(self, hayvan):
        self.evcil_hayvanlar.append(hayvan)
        hayvan.sahip = self

    def __str__(self):
        return f"{self.ad} {self.soyad} {self.id}"
    
ali = Insan("ali", "veli", 20, 1231312)
ayse = Insan("ayse", "yılmaz", 40, 123131)
boncuk = Kedi("Boncuk", "Tekir", 2)
pasa = Kopek("Paşa", "Golden",4)
ali.sahiplen(boncuk)
ali.sahiplen(pasa)
print(boncuk.sahip)

for hayvan in ali.evcil_hayvanlar:
    print(hayvan)

for hayvan in ayse.evcil_hayvanlar:
    print(hayvan)