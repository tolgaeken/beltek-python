class ogrenci:
    def __init__(self,ad,soyad,sinif,dersNotlari):
        self.ad = ad
        self.soyad = soyad
        self.anneAdi = ""
        self.babaAdi = ""
        self.sinif = sinif
        self.dersNotlari = dersNotlari
        self.ortalama = 0

    def __str__(self):
        return f"{self.ad} {self.soyad} {self.ortalama}"

    def ortHesapla(self):
        ortalamalar = []
        for i,j in self.dersNotlari.items():
            dersNotu = (j["Vize"] * 0.3) + (j["Proje"] * 0.1) + (j["Final"] *0.6)
            ortalamalar.append(dersNotu)
        
        dersNot = sum(ortalamalar)/len(ortalamalar)
        self.ortalama = round(dersNot,2)


    def alinanDersleriYaz(self):
        for i,j in self.dersNotlari.items():
            print(i)

    def tumDersNotlariniYaz(self):
        for i,j in self.dersNotlari.items():
            print(i)
            for i2,j2 in j.items():
                print(i2,j2)
            print("-")



notlar ={"mat101":{"Vize":50,
                    "Proje":40,
                    "Final" : 70},
            "fiz101":{"Vize":70,
                    "Proje":80,
                    "Final" : 65}}

ogr = ogrenci("Tolga","Ç","1",notlar)
print(ogr)
print("---")
ogr.ortHesapla()
print(ogr.ortalama)
print("---")
ogr.alinanDersleriYaz()
print("---")
ogr.tumDersNotlariniYaz()