isim = input("Adınızı giriniz\n")
soyisim = input("Soyadınızı giriniz\n")
yas = int(input("Yaşınızı giriniz\n"))

def isimSoyisimYas(ad,soyad,yasi):
    print(f"Merhaba {ad} {soyad} {yasi}")


isimSoyisimYas(isim,soyisim,yas)
isimSoyisimYas(soyad=soyisim,yasi=yas,ad=isim)
