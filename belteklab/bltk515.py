# dogumGunu = int(input("Doğum gününüzü giriniz\n"))

# def topla():
#     global dogumGunu
#     toplam = kareAl(dogumGunu) + dogumGunu
#     return toplam

# def kareAl(dogumGunuKaresi):
#     dogumGunuKaresi = dogumGunuKaresi ** 2
#     return dogumGunuKaresi

# print(topla())

dogumGunu = int(input("Doğum gününüzü giriniz\n"))

def topla(sayi):
    return kareAl(sayi) + sayi

def kareAl(sayi):
    return sayi ** 2

print(topla(dogumGunu))