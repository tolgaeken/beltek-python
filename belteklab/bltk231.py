# ad = input("Adınızı giriniz \t")
# soyad = input("Soyadınızı giriniz \t")
# yas = int(input("Yaşınızı giriniz \t"))
# print(f"Adınız {ad}\nSoyadınız {soyad}\nYaşınız {yas}\nŞanslı Sayı = {yas*5}")



# yetkiliKisi = "admin"
# yetkiliKisiParola = "123abc"

# kullaniciAdi = input("Kullanıcı Adı giriniz\t")
# parola = input("Parola giriniz\t")

# if(yetkiliKisi == kullaniciAdi):
#     if(parola==yetkiliKisiParola):
#         print("Giriş başarılı")
#     else:
#         print("Parola yanlış")
# else:
#     print("Kullanıcı adı doğru değildir")

ortalama = float(input("Ortalama giriniz\t"))

if(ortalama >= 3.5 and ortalama <= 4):
    print("Kayıt başarılı")
elif (ortalama> 2.7 and ortalama< 3.5):
    print("Sınava girin")
elif(ortalama<=2.7 and ortalama>=0):
    print("Başarısız")
else:
    print("Hatalı giriş")