from datetime import datetime, date
calismalar = []


def yukle():
    global calismalar
    calismalar = []
    with open("calismalarim.txt", "r") as f:
        content = f.read().split("\n")[:-1]
        for i in content:
            i = i.split(", ")
            calismalar.append(i)

    
def kaydet():
    global calismalar
    with open("calismalarim.txt", "a") as f:
        for calisma in calismalar:
            f.write(f"{calisma[0]}, {calisma[1]}, {calisma[2]}, {calisma[3]}\n")

            
def ara(kategori):
    global calismalar
    temp = []
    for calisma in calismalar:
        if kategori.lower() == calisma[1].lower():
            temp.append(calisma)
    listele(temp)

    
def listele(liste=None):
    if liste is None:
        global calismalar
        liste = calismalar

    for index, item in enumerate(liste):
        print(f"{index+1}. {item[0]}, {item[1]}, {item[2]}, {item[3]}")

        
menu = """
1. Sayaç başlat
2. Çalışmalarımı listele
3. Kategoriye göre arama yap
4. Çalışmalarımı kaydet
5. Çalışmalarımı yükle
6. Çıkış
"""


while True:
    print(menu)
    girdi = int(input("#"))
    match girdi:
        case 1:
            baslik = input("Çalışma başlığı giriniz:\t")
            kategori = input("Kategori adı giriniz:\t")
            today = date.today()
            start = datetime.now()
            input(f"{str(datetime.today()).split('.')[0]} başlangıç tarihi, sayacı durdurmak için enter tuşuna basınız.")
            finish = str(datetime.now() - start).split(".")[0]
            temp = [baslik, kategori, finish, today]
            calismalar.append(temp)
        case 2:
            listele()
        case 3:
            kategori = input("Aramak istediğiniz kategori adını giriniz:\t")
            ara(kategori)
        case 4:
            kaydet()
        case 5:
            yukle()
        case 6:
            break
