mevsimNo = int(input("""Mevsim Giriniz
İlkbahar için 1
Yaz için 2
Sonbahar için 3
Kış için 4 giriniz\n"""))

kalinacakGunSayisi = int(input("""Kalınacak gün sayısını seçiniz
3 gün kalınacaksa 3
5 gün kalınacaksa 5 giriniz\n"""))

if(kalinacakGunSayisi == 1):
    if(mevsimNo==1):
        ucret = 200
    elif(mevsimNo==2):
        ucret = 400
    elif(mevsimNo==3):
        ucret = 180
    elif(mevsimNo==4):
        ucret = 300
    else:
        print("Mevsim seçimini hatalı girdiniz")

    print(f"Otelin ücreti {ucret} ₺")

elif(kalinacakGunSayisi==2):
    if(mevsimNo==1):
        ucret = 310
    elif(mevsimNo==2):
        ucret = 750
    elif(mevsimNo==3):
        ucret = 750
    elif(mevsimNo==4):
        ucret = 500
    else:
        print("Mevsim seçimini hatalı girdiniz")

    print(f"Otelin ücreti {ucret} ₺")

else:
    print("Kalınacak gün seçilirken hatalı bir seçim yaptınız")