menu = """
1. Kitap ekle
2. Kitapları listele
3. Kitap sil
4. Çıkış
"""

def kayıt_et_global():
    global kitaplar
    with open("kitaplar.txt", "w") as f:
        for index, kitap in enumerate(kitaplar):
            f.write(f"{index+1}. {kitap[0]}, {kitap[1]}, {kitap[2]}\n")

def kayıt_et_parametre(kitaplar_listesi):
    with open("kitaplar.txt", "w") as f:
        for index, kitap in enumerate(kitaplar_listesi):
            f.write(f"{index+1}. {kitap[0]}, {kitap[1]}, {kitap[2]}\n")

kitaplar = []
while True:
    print(menu)
    girdi = int(input("#"))
    match girdi:
        case 1:
            kitap_ad = input("Kitap adı giriniz:\t")
            yazar_ad = input("Yazar adı giriniz:\t")
            sayfa_sayisi = int(input("Sayfa sayısı giriniz:\t"))

            temp = [kitap_ad, yazar_ad, sayfa_sayisi]
            kitaplar.append(temp)
            print("Kitap eklendi.")
        case 2:
            for index, kitap in enumerate(kitaplar):
                print(f"{index+1}, {kitap[0]}, {kitap[1]}, {kitap[2]}")
        case 3:
            silinecek = int(input("Silinecek kitap sırasını giriniz"))-1
            del kitaplar[silinecek]
            print("Kitap silindi.")
        case 4:
            print("Kaydediliyor...")
            kayıt_et_parametre(kitaplar)
            print("Çıkış yapılıyor...")
            break

