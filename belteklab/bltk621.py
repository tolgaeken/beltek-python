def listeMaxSayi(liste):
    i=0
    for sayi in liste:
        if(sayi>i):
            i= sayi
    return i

list = [3,7,22,1,9,6]

print(listeMaxSayi(list))
