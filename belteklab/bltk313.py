cokgenTip = int(input("""Çokgenin kaç kenarlı olduğunu belirtiniz
Üçgen ise 3
Dörtgen ise 4 giriniz\n\n"""))

if cokgenTip == 3:
    taban = int(input("Taban kenar uzunluğunu giriniz\n"))
    yukseklik = int(input("Yüksekliği giriniz\n"))
    alan = (taban*yukseklik) / 2
    print (f"Seçilen çokgen bir üçgendir. Alanı {alan} br karedir")

elif cokgenTip==4:
    dortgentip = int(input("""Dörtgenin kare veya dikdörtgen olduğunu belirtiniz
    Kare ise 1
    Dikdörtgen ise 2 giriniz\n\n"""))
    if dortgentip == 1:
        kenar = int(input("Kenar uzunluğunu giriniz\n"))
        alan = kenar**2
        print(f"Seçilen çokgen bir karedir. Alanı {alan} br karedir")
    elif dortgentip == 2:
        taban = int(input("Taban kenar uzunluğunu giriniz\n"))
        yukseklik = int(input("Yüksekliği giriniz\n"))
        alan = taban * yukseklik
        print(f"Seçilen çokgen bir dikdörtgendir. Alanı {alan} br karedir")
    else:
        print("Girilen değerler hatalıdır")

else:
    print("Girilen çokgen tipi hatalıdır")