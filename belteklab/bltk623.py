from datetime import datetime,date
import time

# calışma başlık, çalışma aktegori,kaç dakika çalışacak, uyku hesaplanacak


def kaydet():
    global calismaliste
    with open("FilePath\\calisma.txt" ,"a") as f:
        for index,calisma in enumerate(calismaListe):
            f.write(f"{index+1}. {calisma[0],calisma[1],calisma[2]} \n")

calismaListe = []

menu = int(input("1 - Çalışma Başlat\n2 - Çalışma Listele\n3 - Kaydet\n"))

match(menu):
    case 1:
        baslik = input("Çalışma başlığı giriniz\n")
        kategori = input("Çalışma kategorisi giriniz\n")
        sure = input("Süreyi giriniz, süreyi dakika:saniye cinsinden yazınız\n")
        tarih = date.today()
    
        saniye = (int(sure.split(":")[0])*60) + int(sure.split(":")[1])
        temp = [baslik,kategori,sure,tarih]
        
        time.sleep(saniye)

        calismaListe.append(temp)

    case 2:
        for i,calisma in enumerate(calismaListe):
                for item in calisma:
                    print((i+1),",".join(calisma), end="*\n")

    case 3:
        kaydet()




# for index, calisma in enumerate(calismaListe):
# print(index+1, end=". ")
# for item in calisma:
#     print(str(item), end=" ")