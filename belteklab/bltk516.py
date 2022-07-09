from random import randrange

baslangic = int(input("Başlangıç sayısı giriniz\n"))
bitis = int(input("Bitiş sayısı giriniz\n"))

while True:
    if(baslangic<bitis):
        a = randrange (baslangic,bitis)
        print(a)
    else:
        print("Bitiş değer başlangıç değerinden büyük")
        break