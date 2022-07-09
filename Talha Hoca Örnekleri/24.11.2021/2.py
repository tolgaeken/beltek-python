class Ogrenci:
    def __init__(self, ad, soyad, sinif, ders_notlari):
        self.ad = ad
        self.soyad = soyad
        self.sinif = sinif
        self.ders_notlari = ders_notlari
        self.anne_adi = ""
        self.baba_adi = ""
        self.ortalama = 0

    def ortalama_hesapla(self):
        toplam = 0
        ders_sayisi = 0

        for puanlar in self.ders_notlari.values():
            toplam += puanlar["vize"] * 0.3 + puanlar["proje"] * 0.1 + puanlar["final"] * 0.6
            ders_sayisi += 1
        
        self.ortalama = toplam / ders_sayisi

    
    def dersleri_yaz(self):
        print(f"{self.ad}'ın dersleri yazdırılıyor")
        for ders in self.ders_notlari.keys():
            print(ders)

    def notlari_yaz(self):
        print(f"{self.ad}'ın ders notları yazdırılıyor")
        for ders_kodu, puanlar in self.ders_notlari.items():
            print(f"{ders_kodu}: V:{puanlar['vize']}, P:{puanlar['proje']}, F:{puanlar['final']}")

    def __str__(self):
        return f"{self.ad} {self.soyad} {self.ortalama}"



dersler = {"MAT 101": {
        "vize": 100,
        "final": 40,
        "proje": 65
    },
    "MAT 201": {
        "vize": 100,
        "final": 100,
        "proje": 100
    },
    "MAT 301": {
        "vize": 20,
        "final": 100,
        "proje": 85
    }
}


ogrenci1 = Ogrenci("Burak", "Yılmaz", 3, dersler)
ogrenci1.anne_adi = "Fatma"
ogrenci1.baba_adi = "Necmi"
print("Hesaplamadan önce", ogrenci1.ortalama)
ogrenci1.ortalama_hesapla()
print("Hesaplamadan sonra", ogrenci1.ortalama)
ogrenci1.dersleri_yaz()
ogrenci1.notlari_yaz()
print(ogrenci1)