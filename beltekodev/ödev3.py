mezuniyetNotu = float(input("Mezuniyet notu giriniz : \t"))
birinciSinavPuani = float(input("Birinci sınav notu giriniz : \t"))
ikinciSinavPuani = float(input("İkinci sınav notu giriniz : \t"))
sinavPuanOrt = float((birinciSinavPuani * 0.4) + (ikinciSinavPuani * 0.6))


if(mezuniyetNotu >= 70 and mezuniyetNotu <=100):
    if((sinavPuanOrt >= 420.5) and (sinavPuanOrt <= 500)):
        yabanciDilGecmeDurumu = int(input("Yabancı dil sınavını başarı ile geçtiniz mi (Evet ise 1'e, hayır ise 2'ye basınız)? \t"))
        if(yabanciDilGecmeDurumu == 1):
            print("Aramıza hoş geldiniz! Bölüm dersi seçebilirsiniz.")
        elif(yabanciDilGecmeDurumu == 2):
            print("Aramıza hoş geldiniz! Hazırlık dersleri almanız gerekmektedir.")
        else:
            print("Yabancı dil geçme durumunda hatalı giriş yaptınız.")
    elif(sinavPuanOrt<420.5 and sinavPuanOrt>380.5):
        print("Aramıza hoş geldiniz! Yeterlilik sınavına girmeniz gerekmektedir.")
    elif(sinavPuanOrt<=380.5 and sinavPuanOrt >=0):
        print("Aramıza hoş geldiniz! Bilimsel hazırlık dersleri almanız gerekmektedir.")
    else:
        print("Hatalı sınav notu girişi yaptınız.")
elif(mezuniyetNotu<70 and mezuniyetNotu >=0):
    print("Maalesef üniversitemize kayıt yaptıramazsınız.")
else:
    print("Hatalı mezuniyet notu girdiniz.")
