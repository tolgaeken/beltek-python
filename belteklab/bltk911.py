class Banka:
    def __init__(self,bankaAdi):
        self.bankaAdi = bankaAdi
        self.bankaHesaplari = []
        self.bankaMusterileri = []
    
    def hesapEkle(self,bankaHesap):
        hesapIdler = []
        for hesaplar in self.bankaHesaplari:
            hesapIdler.append(hesaplar[0])

        if bankaHesap.id not in hesapIdler:
            self.bankaHesaplari.append(bankaHesap)
            bankaHesap.banka = self
        
        else:
            print("Girmiş olduğunuz Id daha önce kullanılmıştır")

    def musteriEkle(self,musteri):
        musteriIdler = []
        for musteri in self.bankaMusterileri:
            musteriIdler.append(musteri[0])
        
        if musteri.id not in musteriIdler:
            self.bankaMusterileri.append(musteri)
        
        
        else:
            print("Girmiş olduğunuz Id daha önce kullanılmıştır")

    def paraGonder(self,gonderenHesap,alanHesap,miktar):
        if gonderenHesap.bakiye - miktar >=0:
            print(f"{gonderenHesap.musteri} isimli müşteriden, {alanHesap.musteri} isimli müşteriye {gonderenHesap.cins} para gönderilmiştir")
            gonderenHesap -= gonderenHesap
            alanHesap += alanHesap
        
        else:
            print("Yetersiz bakiye")

class BankaHesap:
    def __init__(self,id,musteri,cins):
        self.id = id
        self.musteri = musteri
        self.cins = cins
        self.banka = None
        self.bakiye = 0
    
    def paraYatir(self,miktar):
        self.bakiye += miktar
        print(f"Bakiyeniz : {self.bakiye} {self.cins}")

    def paraCek(self,miktar):
        if self.bakiye - miktar >=0:
            self.bakiye -= self.bakiye
            print(f"Bakiyeniz : {self.bakiye} {self.cins}")
        
        else:
            print("Yetersiz bakiye")


class Musteri:
    def __init__(self,id,ad,soyad):
        self.id = id
        self.ad = ad
        self.soyad = soyad
        self.hesaplar = []

a = Musteri()
a.hesaplar.append(BankaHesap())