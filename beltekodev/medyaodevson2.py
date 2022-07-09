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
            f.write(f"{hesap[0]}, {hesap[1]}, {hesap[2]}, {hesap[3]}, {hesap[4]}\n")

def listele():
    if len(hesaplar) > 0:
        for index, hesap in enumerate(hesaplar):
            print(f"{index+1}. {hesap[0]}, {hesap[1]}, {hesap[2]}, {hesap[3]}, {hesap[4]}")
    else:
        print("Hiçbir girdi bulunamadı.")

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

def parolauret(karakterUzunluk):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    parola =""
    for i in range(karakterUzunluk+1):
        parola+=random.choice(karakterler)
    
    return parola  

def guncelle():
    pass

def sil():
    pass


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
            pass

        case 4:
            pass   

        case 5:
            pass
        
        case 6:
            kaydet()

        case 7:
            dosyadanyukle()

        case 8:
            break
