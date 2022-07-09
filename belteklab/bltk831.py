class insan:
    def __init__(self,ad,soyad,yas,tcKimlik):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.meslek = ""
        self.tcKimlik = tcKimlik
        self.kanGrubu = ""
        self.evcilHayvanlar = []
    
    def __str__(self):
        return f"{self.ad} {self.soyad} {self.tcKimlik}"

    def hayvanSahiplen(self,hayvan):
        self.evcilHayvanlar.append(hayvan)
        hayvan.sahip = self
        

class kopek:
    def __init__(self,ad,cins,yas):
        self.ad = ad
        self.cins = cins
        self.yas = yas
        self.asilar = False
        self.renk = ""
        self.sahip = None
    
    def __str__(self):
        return f"{self.ad} {self.cins} {self.yas}"

class kedi:
    def __init__(self,ad,cins,yas):
        self.ad = ad
        self.cins = cins
        self.yas = yas
        self.asilar = False
        self.renk = ""
        self.sahip = None
    
    def __str__(self):
        return f"{self.ad} {self.cins} {self.yas}"

kisi = insan("Tolga","E",30,1112548)
kisi.meslek = "Ogretmen"
kisi.kanGrubu = "B+"

zeytin = kopek("Zeytin","Golden",3)
zeytin.asilar = True
zeytin.renk = "Gri"
kisi.hayvanSahiplen(zeytin)

boncuk = kedi("Boncuk","Tekir",1)
boncuk.asilar = False
boncuk.renk = "Beyaz"
kisi.hayvanSahiplen(boncuk)

print(zeytin.sahip)
