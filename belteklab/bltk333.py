#1.soru
for i in range(1,29):
    if i%2==1 :
        print(i)

# -----------------

#2.soru
i=1
while (i<28):
    if(i%2==1):
        print(i)
    i+=1

# -----------------

# 3.soru
sebzeler = []

# 5.soru
sebzeler.append("Ispanak")
sebzeler.append("Patlıcan")
sebzeler.append("Kabak")

# 6.soru
print(sebzeler[2])

# 8.soru
i=0
while(i<len(sebzeler)):
    print(f"{i}. sebze : {sebzeler[i]}")
    i+=1

# -----------------

# 4.soru
meyveler = ["armut","kivi","elma","muz","kavun","karpuz"]

# 7.soru
for i,j in enumerate(meyveler):
    print(f"{i}. indisteki meyvenin adı : {j}")

# -----------------

# 9.soru
kitapSayisi = int(input("Kaç adet kitap girişi yapılacaktır\n"))
kitapAdi = []
kitapYazari = []

i = 0

while(i<kitapSayisi):
    kitapAdi.append(input(f"{i+1}. Kitabın adını giriniz\t")) 
    kitapYazari.append(input(f"{i+1}. Kitabın yazarını giriniz\t"))
    i+=1

i = 0

print("\n\nKitap Bilgileri\n\n")

while (i<kitapSayisi):
    print(f"{i+1}. Kitap :  {kitapAdi[i]}   ,Yazarı : {kitapYazari[i]}")
    i+=1

# -----------------

# 10.soru
arkadasListesi = []

while True:
    arkadasListesi.append(input("Lütfen bir arkadaşınızın tam adını giriniz\t").lower())
    if arkadasListesi[-1]=="çıkış":
        break

print(f"{(len(arkadasListesi)-1)} arkadaşınız var")

#Hocanın metodu
arkadasListesi = []

while True:
    girdi = input("Arkadaşınızın adını yazınız, çıkmak için çıkış yazınız: \t")
    girdi = girdi.lower()
    if girdi == "cikis":
        break
    arkadasListesi.append(girdi)

print(f"{len(arkadasListesi)} arkadaşınız var")

for i in arkadasListesi:
    print(i)
