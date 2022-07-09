arkadasListesi = []

for i in range(10):
    isim = input(f"{i+1}. Arkadaşınızın adını giriniz\n")
    arkadasListesi.append(isim)


with open ("bltk815arkadasekleme.txt","a") as f:
    for i in arkadasListesi:
        f.write(i + "\n")

# with open ("bltk815arkadasekleme.txt","w") as f:
#     dosyaIcerik = "\n".join(arkadasListesi)
#     f.write = dosyaIcerik

mesaj = ",".join(arkadasListesi)
print(mesaj)