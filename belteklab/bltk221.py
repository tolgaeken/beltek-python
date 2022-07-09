# s1 = int(input("ilk sayıyı giriniz : \t"))
# s2 = int(input("ikinci sayıyı giriniz : \t"))
# ho = (2*(s1*s2))/(s1+s2)

# # print("Harmonik ortalama : \t" ,format(ho,".4f"))
# # print(f"ilk sayı {s1}, ikinci sayı {s2}")
# print(f"iki sayının toplamı \t {s1+s2}")

# # a = "ali"
# # b = "veli"

# # print(f"ilk isim {a}, ikinci isim {b}")

# gun = input("gün giriniz \t")
# havaDurumu = input("hava durumu giriniz\t")
# print(f"{gun} günü hava {havaDurumu} görünüyor")


# birinciKenar = int(input("birinci kenarı giriniz\t"))
# ikinciKenar = int(input("ikinci kenarı giriniz\t"))
# kosegen = ((birinciKenar*birinciKenar)+(ikinciKenar*ikinciKenar))**(1/2)
# print(f"alanı {birinciKenar*ikinciKenar} br karedir")
# print(f"köşegen uzunluğu {kosegen:.4f}")

birinciKenar = int(input("birinci kenarı giriniz\t"))
ikinciKenar = int(input("ikinci kenarı giriniz\t"))
kosegen = round(((birinciKenar*birinciKenar)+(ikinciKenar*ikinciKenar))**(1/2),4)
print(f"alanı {birinciKenar*ikinciKenar} br karedir")
print(f"köşegen uzunluğu {kosegen}")



girilensayi = input("Bir sayi girin")

sayiyacevir = int(girilensayi)


carpim = 1

for i in range(1,sayiyacevir+1):
    # toplam = toplam + i
    carpim *= i

print(carpim)