class Kedi:
    def __init__(self, ad, cins, cinsiyet, kedi_rengi, kuyruk, ayak_sayisi):
        self.ad = ad
        self.cins = cins
        self.cinsiyet = cinsiyet
        self.renk = kedi_rengi
        self.kuyruk = kuyruk
        self.ayak_sayisi = ayak_sayisi
        self.asilar = False

    def miyavla(self, miyavlama_tipi, miyavlama_sayisi):
        print(f"{self.ad} miyavlıyor...")
        print((miyavlama_tipi + " ") * miyavlama_sayisi)

    def pati_at(self):
        print(f"{self.ad} pati attı")

    def uyu(self):
        print(f"{self.ad} uyuyor...")

    def __str__(self):
        return f"Kedi: {self.ad}, {self.cins}, {self.renk}"


tekir = Kedi("Tekir","tekir","Erkek","Beyaz",True,4)
tekir.asilar = True
paris = Kedi("Paris", "Scottish","Dişi","Gri", True, 4)




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

for value in dersler.values():
    print(value)