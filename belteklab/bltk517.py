from random import randrange

ogrListe = []

for i in range(0,45):
    rastgele = randrange(0,100)
    ogrListe.append(rastgele)

ortalama = sum(ogrListe) / len(ogrListe)
print(round(ortalama,2))


def mezun(derece):
    global ortalama
    if(derece>= ortalama):
        print("Mezun")
    else:
        print("Mezun değil")

for j,k in enumerate(ogrListe):
    print(j+1,k,end = " ")
    mezun(k)
