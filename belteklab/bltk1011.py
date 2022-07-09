class Insan:
    def __init__(self,kimlikNo,ad,soyad,yas = None):
        self.kimlikNo = kimlikNo
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
    
    def __str__(self) -> str:
        return f"Kimlik No : {self.kimlikNo} - Adı : {self.ad} - Soyadı : {self.soyad} - Yaş : {self.yas} "

class Ogrenci(Insan):
    def __init__(self, kimlikNo, ad, soyad, yas=None , ortalama = None):
        super().__init__(kimlikNo, ad, soyad, yas=yas)
        self.ortalama = ortalama
        self.aldigiDersler = []
    
    def __str__(self) -> str:
        return super().__str__() + f"- Ortalaması : {self.ortalama}"

class Ogretmen(Insan):
    def __init__(self, kimlikNo, ad, soyad, yas=None,brans = None):
        super().__init__(kimlikNo, ad, soyad, yas=yas)
        self.brans = brans
        self.girdigiSiniflar = dict()
        self.verdigiDersler = []
        self.kidem = 0

    def dersEkle (self,ders):
        self.verdigiDersler.append(ders)
        ders.ogretmen = self


    def __str__(self) -> str:
        return super().__str__() + f"- Branşı : {self.brans} - Giridği Sınıflar : {self.girdigiSiniflar} - Verdiği Dersler : {self.verdigiDersler} - Kıdemi : {self.kidem}"

class Ders:
    def __init__(self,kod,ad,kredi):
        self.kod = kod
        self.ad = ad
        self.kredi = kredi
        self.ogretmen = None
        self.ogrenciler = []
    
    def ogrenciEkle(self,ogrenci):
        self.ogrenciler.append(ogrenci)
        ogrenci.aldigiDersler.append(self)
    
    def __str__(self) -> str:
        return f"{self.ogrenciler}"

    

insan1 = Insan(123,"Ali","Veli",28)
ogrenci1 = Ogrenci(456,"Ahmet","Mehmet",23,3)
ogretmen1 = Ogretmen(789,"Fatih","Bulut",34,"Bil Müh")
ogretmen1.kidem = 3
ders1 = Ders("COMP101","Bil Müh Giriş",6)
ders1.ogrenciEkle(ogrenci1)

print(ders1)

