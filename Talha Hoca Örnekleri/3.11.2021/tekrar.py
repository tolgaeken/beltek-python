from random import randrange

def random_elemanli_list_uret(eleman_sayisi, en_kucuk, en_buyuk):
    temp = []
    for a in range(0,eleman_sayisi):
        rand_item = randrange(en_kucuk,en_buyuk)
        temp.append(rand_item)
    return temp

def toplama(elements):
    toplam = 0
    for i in elements:
        toplam += i
    return toplam

def boyut_hesapla(elements):
    eleman_sayisi = 0
    for i in elements:
        eleman_sayisi+=1

    return eleman_sayisi

def ortalama(elements):
    ortalama = toplama(elements) / boyut_hesapla(elements)
    return ortalama


rand_list = random_elemanli_list_uret(100, 1, 1000)
rand_list1 = random_elemanli_list_uret(20, 10, 40)
