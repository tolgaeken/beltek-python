class Insan:
    def __init__(self, ad, soyad, TCKN, kan_grubu) -> None:
        self.ad = ad
        self.soyad = soyad
        self.TCKN = TCKN
        self.kan_grubu = kan_grubu


    def __str__(self):
        return f"{self.ad} {self.soyad} {self.TCKN}"

class Ogrenci(Insan):
    def __init__(self, ad, soyad, TCKN, kan_grubu, gpa) -> None:
        super().__init__(ad, soyad, TCKN, kan_grubu)
        self.gpa = gpa


class Ogretmen(Insan):
    def __init__(self, ad, soyad, TCKN, kan_grubu, brans) -> None:
        Insan.__init__(self, ad, soyad, TCKN, kan_grubu)
        self.brans = brans

    def __str__(self):
        return super().__str__() + f" bras: {self.brans}"

insan = Insan("Ali", "Veli", 2231231, "B+")
print(insan)
ogrenci = Ogrenci("Şakir", "Saklı", 123456, "A+", 3.12)
print(ogrenci)
print(ogrenci.gpa)
ogretmen = Ogretmen("Ayşe", "Yıldırım", 231123, "A-", "Matematik")
print(ogretmen)