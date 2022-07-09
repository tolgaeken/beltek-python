import random
import string

hesaplar = []

def dosyadanyukle():
    global hesaplar
    with open("sosyalmedya.txt","r") as f:
        file_content = f.read().split('\n')[:-1]
        
        for line in file_content:
            line = line.split(", ")
            hesaplar.append(line)

def kaydet():
    global hesaplar
    with open("sosyalmedya.txt","w") as f: 
        for hesap in hesaplar:
            f.write(f"{hesap[0]}, {hesap[1]}, {hesap[2]}, {hesap[3]}, {hesap[4]}\n")

def listele():
    if len(hesaplar) > 0:
        for index, hesap in enumerate(hesaplar):
            print(f"{index+1}. {hesap[0]}, {hesap[1]}, {hesap[2]}, {hesap[3]}, {hesap[4]}")
    else:
        print("Hiçbir girdi bulunamadı.\n")

def ayniParolaliHesaplarListele():
    sifreListe = []
    ayniSifreler = []
    for hesap in hesaplar:
        if hesap[4] in sifreListe:
            ayniSifreler.append(hesap[4])
        else:
            sifreListe.append(hesap[4])
    
    for index, hesap in enumerate(hesaplar):
        if hesap[4] in ayniSifreler:
            print(f"{index+1}. {hesap[0]}, {hesap[1]}, {hesap[2]}, {hesap[3]}, {hesap[4]}")

def baslikBul():
    basliklar = []
    for hesap in hesaplar:
        if hesap[0] not in basliklar:
            basliklar.append(hesap[0])

    for index,baslik in enumerate(basliklar):
        print(f"{index+1} - {baslik}")
    
    baslikNo = int(input("Lütfen yukarıdan bir başlık seçiniz\n")) -1

    for hesap in hesaplar:
        if hesap[0] == basliklar[baslikNo]:
            print(hesap)

def urlBul():
    urller = []
    for hesap in hesaplar:
        if hesap[1] not in urller:
            urller.append(hesap[1])

    for index,url in enumerate(urller):
        print(f"{index+1} - {url}")
    
    urlNo = int(input("Lütfen yukarıdan bir url seçiniz\n")) -1

    for hesap in hesaplar:
        if hesap[1] == urller[urlNo]:
            print(hesap)

def kategoriBul():
    kategoriler = []
    for hesap in hesaplar:
        if hesap[2] not in kategoriler:
            kategoriler.append(hesap[2])

    for index,kategori in enumerate(kategoriler):
        print(f"{index+1} - {kategori}")
    
    kategoriNo = int(input("Lütfen yukarıdan bir kategori seçiniz\n")) -1

    for hesap in hesaplar:
        if hesap[2] == kategoriler[kategoriNo]:
            print(hesap)

def kullaniciAdiBul():
    kullaniciAdlari = []
    for hesap in hesaplar:
        if hesap[3] not in kullaniciAdlari:
            kullaniciAdlari.append(hesap[3])

    for index,kullaniciAdi in enumerate(kullaniciAdlari):
        print(f"{index+1} - {kullaniciAdi}")
    
    kullaniciAdiNo = int(input("Lütfen yukarıdan bir kullanıcı adı seçiniz\n")) -1

    for hesap in hesaplar:
        if hesap[3] == kullaniciAdlari[kullaniciAdiNo]:
            print(hesap)

def parolauret(karakterUzunluk):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    parola =""
    for i in range(karakterUzunluk+1):
        parola+=random.choice(karakterler)
    
    return parola  

def guncelle(hesapNo,hesap):
    global hesaplar
    baslik = input("Başlık Giriniz\n")
    url = input("URL Giriniz\n")
    kategori = input("Kategori Giriniz\n")
    kullaniciAdi = input("Kullanıcı Adı Giriniz\n")
    parolaMenu = int(input("""
    1 - Rastgele 15 haneli parola üret
    2 - Yeni parola gir\n"""))
    match(parolaMenu):
        case 1:
            parola = parolauret(15)
            print(f"Parolanız : {parola}")
        case 2:
            parola = input("Parola giriniz\n")
            print(f"Parolanız : {parola}")
    
    del hesaplar[hesapNo]
    hesap = (baslik,url,kategori,kullaniciAdi,parola)
    hesaplar.insert(hesapNo,hesap)

def sil(hesap):
    global hesaplar
    silmeOnay = input(f"""Kullanıcı adı '{hesaplar[hesap][3]}' 
        olan kullanıcıyı silmek istediğinize emin misiniz?Evet ise 'e' yazınız""").lower()

    if silmeOnay == "e":
        del hesaplar[hesap]
        print("Hesap silindi...\n")


while True:
    menu = int(input("""
    1 - Hesap Ekle
    2 - Hesapları Listele
    3 - Hesap Güncelle
    4 - Hesap Bul
    5 - Hesap Sil
    6 - Verileri Kaydet
    7 - Verileri Yükle
    8 - Çıkış\n"""))

    match(menu):
        case 1:
            baslik = input("Başlık Giriniz\n")
            url = input("URL Giriniz\n")
            kategori = input("Kategori Giriniz\n")
            kullaniciAdi = input("Kullanıcı Adı Giriniz\n")
            parolaMenu = int(input("""
            1 - Rastgele 15 haneli parola üret
            2 - Yeni parola gir"""))
            match(parolaMenu):
                case 1:
                    parola = parolauret(15)
                    print(f"Parolanız : {parola}")
                case 2:
                    parola = input("Parola giriniz\n")
                    print(f"Parolanız : {parola}")
            
            temp = (baslik,url,kategori,kullaniciAdi,parola)
            hesaplar.append(temp)
        
        case 2:
            listeMenu = int(input("""
            Tümünü listelemek için 1'i
            Aynı parolaya sahip hesapları listelemek için 2'ye basınız\n"""))
            match (listeMenu):
                case 1:
                    listele()
                case 2:
                    ayniParolaliHesaplarListele()
                            
        case 3:
            if(len(hesaplar)==0):
                print("Mevcut bir hesap bulunmamaktadır\n")
                continue

            listele()
            hesapNo = int(input("Düzenlemek istediğiniz hesabın numarasını giriniz\n"))-1
            guncelle(hesapNo,hesaplar[hesapNo])

        case 4:
            bulMenu = int(input("""
            1 - Başlığa göre bul
            2 - URL'e göre bul
            3 - Kategoriye göre bul
            4 - Kullanıcı adına göre bul
            """))
            match(bulMenu):
                case 1:
                    baslikBul()
                case 2:
                    urlBul()
                case 3:
                    kategoriBul()
                case 4:
                    kullaniciAdiBul()

        case 5:
            if(len(hesaplar)==0):
                print("Mevcut bir hesap bulunmamaktadır\n")
                continue
            
            listele()

            hesapNo = int(input("Silmek isteidiğiniz hesap numarasını giriniz\n"))-1

            if(len(hesaplar)<hesapNo):
                print(f"{len(hesaplar)} adet hesap vardır {hesapNo+1} numaralı hesap geçersizdir\n")
                continue

            sil(hesapNo)
        
        case 6:
            kaydet()

        case 7:
            dosyadanyukle()

        case 8:
            break
