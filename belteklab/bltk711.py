from random import randrange

bogaSayisi = 0
danaSayisi = 0

def bogaDanaHesapla(girdi,rastgeleSayi):
    global bogaSayisi,danaSayisi

    for i in range(4):
        if (str(girdi)[i] == str(rastgeleSayi)[i]):
            danaSayisi+=1

        elif(str(girdi)[i] in str(rastgeleSayi)):
            bogaSayisi+=1
        
    return girdi,rastgeleSayi

while True:

    girdi = int(input("Rastgele Sayı Giriniz\nBu Sayı 4 Haneli Olmalıdır\n"))
    
    if (len(str(girdi))) != 4:
        print("Girilen sayı 4 haneli değildir!!\n")
        continue

    rastgeleSayi = randrange(1000,10000)
    
    bogaDanaHesapla(girdi,rastgeleSayi)

    print(f"Boğa Sayısı : {bogaSayisi}")
    print(f"Dana Sayısı : {danaSayisi}")

    if(danaSayisi==4):
        print("Dana sayısı 4 olmuştur.\n")
        break

    

