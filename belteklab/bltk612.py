from datetime import date,datetime
import time

def kaydetGlobal():
  global calismalar
  with open("FilePath\\calisma.txt" ,"w") as f:
    for index,calisma in enumerate(calismalar):
      f.write(f"{index+1}. {calisma[0],calisma[1],calisma[2],calisma[3]} \n")

def kaydetParametre(calismaListe):
  with open("FilePath\\calisma.txt" ,"w") as f:
    for index,calisma in enumerate(calismaListe):
      f.write(f"{index+1}. {calisma[0],calisma[1],calisma[2],calisma[3]} \n")

calismalar = []
kategoriler = []

while True:
    menu = int(input("1 - Sayaç Başlat\n2 - Çalışmalarımı Listele\n3 - Kategoriye Göre Arama Yap\n4 - Çalışmalarımı Kaydet\n5 - Çıkış"))

    match(menu):
        case 1:
            baslik = input("Başlık Giriniz\n")
            kategori = input("Kategori Giriniz\n")
            start = datetime.now()
            finish = input("Sayaç başlamıştır, durdurmak için enter tuşuna basınız\n")
            while True:
                if(finish == ""):
                    finish = datetime.now()
                    break
            tarih = date.today()
            
            sure = str(finish-start).split(".")[0]
            
            if kategori not in kategoriler:
                kategoriler.append(kategori)
                
            temp = [baslik,kategori,sure,tarih]

            calismalar.append(temp)
        case 2:
            for i,calisma in enumerate(calismalar):
                print((i+1),",".join(calisma), end="*\n")
        case 3:
            for i,kategori in enumerate(kategoriler):
                print(f"{i+1}. {kategori}")
            
            kategoriNo = int(input("Yukarıda girilen kategorilerden birini girin"))-1

            for i,calisma in enumerate(calismalar):
                if(i[1] == kategoriNo):
                    print((i+1),",".join(calisma), end="*\n")
        case 4:
            pass
        
        case 5:
            break
