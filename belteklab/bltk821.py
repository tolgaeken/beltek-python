class Kedi:
    def __init__(self,ad,cins,renk,kuyruk,ayakSayisi,cinsiyet):
        self.ad = ad
        self.cins = cins
        self.renk = renk
        self.kuyruk = kuyruk
        self.ayakSayisi = ayakSayisi
        self.cinsiyet = cinsiyet

    def __str__(self):
        return f"Adı: {self.ad}\nCinsi : {self.cins}\nRenk: {self.renk}\nKuyruğu : {self.kuyruk}\nAyak Sayısı {self.ayakSayisi}\nCinsiyet: {self.cinsiyet}"
    
    
    def miyavla(self,miyavlamaTipi,miyavlamasayisi):
        print(f"{self.ad} miyavlıyor")
        print((f"{miyavlamaTipi} ")*miyavlamasayisi)

    def patiAt(self):
        print(f"{self.ad} pati attı")
    
    def uyu(self):
        print(f"{self.ad} uyuyor...")

tekir = Kedi("Tekir","TekirCinsi","Beyaz",True,4,"Erkek")
tekir.ad = "Boncuk"
tekir.miyavla("Miyav",3)
tekir.uyu()

duman = Kedi("Duman","Munchkin","Gri",True,4,"Dişi")
duman.miyavla("Meow",1)
duman.patiAt()


print(duman)