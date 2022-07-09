kitap = dict()

kitap["baslik"] = "Kaşağı"
kitap["yazar"] = "Ömer Seyfettin"
kitap["basim_yili"] = 1908
kitap["sayfa_sayisi"] = 203
kitap["kategori"] = {"a":"c"}

# print(kitap)

kitaplar = dict()

kitaplar["cocuk_kitaplari"] = dict()
kitaplar["cocuk_kitaplari"]["turkce_kitaplar"] = dict()
kitaplar["cocuk_kitaplari"]["turkce_kitaplar"] = kitap

print(kitaplar)