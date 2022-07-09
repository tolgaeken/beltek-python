import random
import string

hesaplar = []

def dosyadanyukle():
    global hesaplar
    with open("sosyalmedya.txt", "r") as f:
        file_content = f.read().split('\n')[:-1]
        
        for line in file_content:
            line = line.split(", ")
            hesaplar.append(line)

def kaydet():
    global hesaplar
    with open("sosyalmedya.txt", "a") as f:
        for hesap in hesaplar:
            f.write(f"{hesap[0]}, {hesap[1]}, {hesap[2]}, {hesap[3]},{hesap[4]}\n")

def listele():
    if len(hesaplar) > 0:
        for index, hesap in enumerate(hesaplar):
            print(f"{index+1}. {hesap[0]}, {hesap[1]}, {hesap[2]}, {hesap[3]},{hesap[4]}")
    else:
        print("Hiçbir girdi bulunamadı.")

def ayniParolaliHesaplarListele():
    sifreListe = []
    ayniSifreler = []
    for hesap in hesaplar:
        if hesaplar[hesap][4] in sifreListe:
            ayniSifreler.append(hesaplar[hesap][4])
        else:
            sifreListe.append(hesaplar[hesap][4])
    
    for index, hesap in enumerate(hesaplar):
        if hesaplar[hesap][4] in ayniSifreler:
            print(f"{index+1}. {hesap[0]}, {hesap[1]}, {hesap[2]}, {hesap[3]},{hesap[4]}")

def parolauret(karakterUzunluk):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    parola =""
    for i in range(karakterUzunluk+1):
        parola+=random.choice(karakterler)
    
    return parola  

def guncelle(hesapNo,hesap):
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
    
    hesap = (baslik,url,kategori,kullaniciAdi,parola)
    hesaplar.insert(hesapNo,hesap)

def sil(hesap):
    global hesaplar
    silmeOnay = input(f"""Kullanıcı adı '{hesap[3]}' 
        olan kullanıcıyı silmek istediğinize emin misiniz?Evet ise 'e' yazınız""").lower()

    if silmeOnay == "e":
        del hesap
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
            listele()
            hesapNo = int(input("Düzenlemek istediğiniz hesabın numarasını giriniz\n"))-1
            guncelle(hesapNo,hesaplar[hesapNo])

        case 4:
            pass

                

        case 5:
            if(len(hesaplar)==0):
                print("Mevcut bir hesap bulunmamaktadır\n")
                continue

            hesapNo = int(input("Silmek isteidiğiniz hesap numarasını giriniz\n"))-1

            if(len(hesaplar)<hesapNo):
                print(f"{len(hesaplar)} adet hesap vardır {hesapNo+1} numaralı hesap geçersizdir\n")
                continue

            sil(hesaplar[hesapNo])
        
        case 6:
            kaydet()

        case 7:
            dosyadanyukle()

        case 8:
            break
