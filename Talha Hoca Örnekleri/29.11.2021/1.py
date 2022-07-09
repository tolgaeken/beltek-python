class Banka:
    def __init__(self, ad) -> None:
        self.ad = ad
        self.hesaplar = []
        self.musteriler = []
        self._hesap_ids = set()
        self._musteri_ids = set()


    def hesap_ekle(self, hesap):
        if hesap.id in self._hesap_ids:
            print("Bu hesap no zaten kayıtlı!")
            return False
        else:    
            self._hesap_ids.add(hesap.id)
            self.hesaplar.append(hesap)
            hesap.banka = self
            print(hesap.id, "ID li hesap", self.ad, "bankasına eklenmiştir.")
            return True


    def musteri_ekle(self, musteri):
        if musteri.id in self._musteri_ids:
            print("Bu ID li müşteri zaten mevcut!")
            return False
        else:
            self._musteri_ids.add(musteri.id)
            self.musteriler.append(musteri)
            print(musteri.id, "ID li müşteri artık", self.ad, "bankasının müşterisidir.")
            return True


    def para_gonder(self, hesaptan, hesaba, miktar):
        if miktar < 1:
            print("Minimum 1 birim para gönderebilirsiniz.")
            return False

        hesaptan = self._hesap_ara(hesaptan)
        hesaba = self._hesap_ara(hesaba)

        if hesaptan != None and hesaba != None:
            sonuc = self.hesaplar[hesaptan].para_cek(miktar)

            if sonuc:
                self.hesaplar[hesaba].para_yatir(miktar)

            return sonuc

        else:
            print("Banka hesaplarından birisi ya da ikisi bulunamadı!")
            return False

    
    def _hesap_ara(self, hesap_no):
        for index, hesap in enumerate(self.hesaplar):
            if hesap.id == hesap_no:
                return index

        return None


    def __str__(self) -> str:
        return f"{self.ad} BANK M: {len(self.musteriler)} H: {len(self.hesaplar)}"        


class BankaHesap:
    def __init__(self, id, musteri, cins) -> None:
        self.id = id
        self.musteri = musteri
        self.cins = cins
        self.bakiye = 0.
        self.banka = None


    def para_yatir(self, miktar):
        if miktar < 0:
            print("Miktar 0'dan büyük olmalıdır.")
            return False

        self.bakiye += miktar
        return True


    def para_cek(self, miktar):
        if miktar > self.bakiye or miktar < 0:
            print("Bakiyenizde olmayan parayı çekemezsiniz ya da miktar < 0 olmalıdır!")
            return False

        self.bakiye -= miktar
        return True


class Musteri:
    def __init__(self, id, ad, soyad) -> None:
        self.id = id
        self.ad = ad
        self.soyad = soyad
        self.hesaplar = []


musteri1 = Musteri(1, "Ali", "Veli")
hesap1 = BankaHesap(1, musteri1, "TL")

musteri2 = Musteri(2, "Fatma", "Güngör")
hesap2 = BankaHesap(2, musteri2, "TL")

banka1 = Banka("BELTEK")

musteri1.hesaplar.append(hesap1)
musteri2.hesaplar.append(hesap2)
banka1.musteri_ekle(musteri1)
banka1.hesap_ekle(hesap1)

banka1.musteri_ekle(musteri2)
banka1.hesap_ekle(hesap2)

hesap1.bakiye = 2000
hesap2.bakiye = 300
print(banka1.hesaplar[0].bakiye)
print(banka1.hesaplar[1].bakiye)

banka1.para_gonder(hesap1.id, hesap2.id, 200)

print(banka1.hesaplar[0].bakiye)
print(banka1.hesaplar[1].bakiye)
