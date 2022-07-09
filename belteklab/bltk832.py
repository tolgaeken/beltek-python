class Holding:
    def __init__(self,ad,ulke):
        self.ad = ad
        self.sirketler = []
        self.ulke = ulke
        self.ceo = None

    def __str__(self) -> str:
        return f"{self.ad} {self.ulke}"
    
    def sirketAta(self,sirket):
        self.sirketler(sirket)
        sirket.holding = self
    
    def ceoAta(self,ceo):
        self.ceo = ceo
        ceo.calistigiYer = self

class Sirket:
    def __init__(self,ad):
        self.ad = ad
        self.holding = None
        self.fabrikalar = []
        self.genelMudur = None

    def __str__(self) -> str:
        return f"{self.ad}"

    def fabrikaAta(self,fabrika):
        self.fabrikalar.append(fabrika)
        fabrika.sirket = self
    
    def genelMudurAta(self,gMudur):
        self.genelMudur = gMudur
        gMudur.calistigiYer = self 

class Fabrika:
    def __init__(self,ad,il):
        self.ad = ad
        self.sirket = None
        self.calisanlar = []
        self.il = il

    def __str__(self) -> str:
        return f"{self.ad} {self.il}"
    
    def isciAta(self,isci):
        self.calisanlar.append(isci)
        isci.calistigiFabrika = self
        
class Isci:
    def __init__(self,id,ad,soyad):
        self.id = id
        self.ad = ad
        self.soyad = soyad
        self.calistigiFabrika = None
    
    def __str__(self) -> str:
        return f"{self.ad} {self.soyad}"

class Insan:
    def __init__(self,ad,soyad):
        self.ad = ad
        self.soyad = soyad
        self.calistigiYer = None
    
    def __str__(self) -> str:
        return f"{self.ad} {self.soyad}"

holding = Holding("TlgHolding","Nicaragua")
holdingCeo = Insan("Tolga","E")
holding.ceoAta(holdingCeo)

sirket1 = Sirket("TlgSirket1")
sirket1Mudur = Insan("Sıla","ss")
sirket1.genelMudurAta(sirket1Mudur)

sirket2 = Sirket("TlgSirket2")
sirket2Mudur = Insan("Akın","aa")
sirket2.genelMudurAta(sirket2Mudur)

fabrika1 = Fabrika("TlgFabrika1","Kastamonu")
isci1 = Isci(123,"Tolga","tlg")
isci2 = Isci(456,"Sıla","sl")
fabrika1.isciAta(isci1)
fabrika1.isciAta(isci2)

fabrika2 = Fabrika("TlgFabrika2","Hatay")
isci3 = Isci(789,"Akın","kn")
isci4 = Isci(321,"Ömer","mr")
fabrika2.isciAta(isci3)
fabrika2.isciAta(isci4)

fabrika3 = Fabrika("TlgFabrika3","Ankara")
isci5 = Isci(654,"ali","l")
isci6 = Isci(987,"Mehmet","mhmt")
fabrika3.isciAta(isci5)
fabrika3.isciAta(isci6)

fabrika4 = Fabrika("TlgFabrika4","İstanbul")
isci7 = Isci(147,"Melis","mls")
isci8 = Isci(258,"Bülent","blnt")
fabrika4.isciAta(isci7)
fabrika4.isciAta(isci8)

print("Holding : ",holding)
print("Holding Ceo : ",holdingCeo)
print("1. Şirket : ",sirket1)
print("1.Şirket Müdürü : ",sirket1Mudur)
print("2. Şirket : ",sirket2)
print("2.Şirket Müdürü : ",sirket2Mudur)
print("1.Fabrika : ",fabrika1)
print("1. İşçi : ",isci1)
print("2. İşçi : ",isci2)
print("2.Fabrika : ",fabrika2)
print("3. İşçi : ",isci3)
print("4. İşçi : ",isci4)
print("3.Fabrika : ",fabrika3)
print("5. İşçi : ",isci5)
print("6. İşçi : ",isci6)
print("4.Fabrika : ",fabrika4)
print("7. İşçi : ",isci7)
print("8. İşçi : ",isci8)