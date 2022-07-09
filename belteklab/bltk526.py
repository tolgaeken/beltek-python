from random import randrange

liste = []

elemanSayiGiris = int(input("Eleman Sayısı Giriniz\n")) 
baslangicGiris = int(input("Başlangıç Sayısı Giriniz\n"))
bitisGiris = int(input("Bitiş Sayısı giriniz\n"))
print()



def restgeleSayiUret(elemanSayisi,baslangic,bitis):
    if(baslangic>bitis):
        tmp = baslangic
        baslangic = bitis
        bitis = tmp
    
    elif(baslangic == bitis):
        bitis+1

    temp = []
    for i in range(0,elemanSayisi):
        rndm = randrange(baslangic,bitis+1)
        temp.append(rndm)
    global liste
    liste = temp
    

def ortalaVeTupleCevir(list):
    toplam = 0
    elemanSayisi = 0
    print(f"Listenin İlk Hali :\t {list}")
    print(f"Listenin ilk tipi :\t {type(list)}")
    popEleman = list.pop()
    list = tuple(list)
    print(f"Listenin Sonraki Hali :\t {list}")
    print(f"Listenin Sonraki tipi :\t {type(list)}")

    for i in list:
        toplam +=i

    for i in list:
        elemanSayisi+=1

    ortalama = round((toplam/elemanSayisi),2)
    print(f"Liste Tipi : {type(list)}")
    print(f"Pop elemanı : {popEleman}")
    print(f"Toplamı : {toplam}")
    print(f"Eleman Sayısı : {elemanSayisi}")
    print(f"Ortalaması : {ortalama}")
    

restgeleSayiUret(elemanSayiGiris,baslangicGiris,bitisGiris)

print(liste)

print(ortalaVeTupleCevir(liste))