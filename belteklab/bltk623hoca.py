from datetime import datetime,date
import time

def calc_time(time_str):
    time_info = time_str.split(":")
    mins = int(time_info[0])
    secs = int(time_info[1])

    return mins*60 + secs


def sleep(secs):
    now = str(datetime.now().hour) + ":" + str(datetime.now().minute)
    print(f"Çalışmaya başlama saati : {now}")
    time.sleep(secs)
    print(f"Çalışma tamamlandı {now}")

def save():
    global studies
    with open ("studies.txt","a") as f:
        for study in studies:
            f.write(f"{study[0], study[1], study[2], study[3]}")


def load():
    global studies
    with open("studies.txt","r") as f:
        file_content = f.read().split()[:-1]
        
        for line in file_content:
            temp = []
            line = line.split(", ")
            for i in line:
                temp.append(i)
            studies.append(line)


menu = """1 - Zamnalayıcı Başlat
2 - Çalışmalarımı Listele
3 - Çalışmalarımı Kaydet
4 - Çalışmalarımı dosyadan yükle
5 - Çıkış
"""

studies = []

while True:
    print(menu)
    girdi = int(input("#"))

    match(girdi) :
        case 1:
            title = input("Çalışma başlığı giriniz\n")
            category = input("Çalışma kategorisi giriniz\n")
            study_time = input("Çalışmak istediğiniz zamanı yazınız dakika:saniye")
            study_time = calc_time(study_time)
            sleep(study_time)
            temp = [title,category,study_time,date.today()]
            studies.append(temp)

        case 2:
            if(len(studies)>0):
                for index,study in enumerate(studies):
                    print(f"{index+1}. {study[0],study[1],study[2],study[3]}")
            
            else:
                print("Hiçbir veir bulunamadı")
        case 3:
            save()
        case 4:
            load()
            print(studies)
        case 5:
            break