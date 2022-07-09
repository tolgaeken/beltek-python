from random import randrange

def boga_dana_hesapla(random_uretilmis_deger, kullanici_deger):
    dana = 0
    boga = 0
    for i in range(4):
        if random_uretilmis_deger[i] == kullanici_deger[i]:
            dana += 1
        elif kullanici_deger[i] in random_uretilmis_deger:
            boga += 1
    return boga, dana

def main():
    random_deger = str(randrange(1000, 9999))
    tahmin_sayac = 0

    while True:
        print(random_deger)
        girdi = input("4 basamaklı bir sayı giriniz, çıkmak için çıkış yazınız:\t")
        if girdi.lower() == "ç":
            break
        if len(girdi) != 4:
            print("girilen değer 4 basamaklı olmalıdır!")
            continue
            
        boga, dana = boga_dana_hesapla(random_deger, girdi)
        tahmin_sayac += 1
        print(f"{boga} tane boga, {dana} tane dana vardır.")

        if dana == 4:
            print(f"Tebrikler! {tahmin_sayac} adımda doğru sonuca ulaştınız.")
            break


main()