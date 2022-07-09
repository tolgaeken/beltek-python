from datetime import datetime, date
import time


def calc_time(time_str):
    time_info = time_str.split(":")
    mins = int(time_info[0])
    secs = int(time_info[1])

    return mins * 60 + secs


def sleep(secs):
    now = str(datetime.now().hour) + ":" + str(datetime.now().minute)
    print(f"Çalışmaya başlama saati: {now}")
    time.sleep(secs)
    now = str(datetime.now().hour) + ":" + str(datetime.now().minute)
    print(f"Çalışma tamamlandı {now}")


def save():
    global studies
    with open("studies.txt", "a") as f:
        for study in studies:
            f.write(f"{study[0]}, {study[1]}, {study[2]}, {study[3]}\n")
    

def load():
    global studies
    with open("studies.txt", "r") as f:
        file_content = f.read().split('\n')[:-1]
        
        for line in file_content:
            line = line.split(", ")
            studies.append(line)




menu = """
1. Zamanlayıcı başlat
2. Çalışmalarımı listele
3. Çalışmalarımı kaydet
4. Çalışmalarımı dosyadan yükle
5. Çıkış
"""
studies = []
while True:
    print(menu)
    girdi = int(input("#"))
    match(girdi):
        case 1:
            title = input("Çalışma başlığı giriniz:\t")
            category = input("Çalışma kategorisini giriniz:\t")
            study_time = input("Çalışmak istediğiniz zamanı yazınız dakika:saniye cinsinde")
            # 20:50
            study_time_in_seconds = calc_time(study_time)
            sleep(study_time_in_seconds)
            temp = [title, category, study_time, date.today()]
            studies.append(temp)
        case 2:
            if len(studies) > 0:
                for index, study in enumerate(studies):
                    print(f"{index+1}. {study[0]}, {study[1]}, {study[2]}, {study[3]}")
            else:
                print("Hiçbir girdi bulunamadı.")
        case 3:
            save()
        case 4:
            load()
        case 5:
            break
