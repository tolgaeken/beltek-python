kitaplar = []

while True:
    girdi = input("Kitap adı giriniz, çıkmak için çıkış yazınız")
    girdi = girdi.lower()

    if(girdi == "çıkış"):
        break

    yazarAdi = input("Yazar adı giriniz")

    temp = [girdi,yazarAdi]

    kitaplar.append = temp

# for kitap in kitaplar:
#     for i in kitap:
#         print(i[0] , i[1] , end="")
#     print("\n" , end="")

for kitap in kitaplar:
    print(f"{kitap[0]} , {kitap[1]}")