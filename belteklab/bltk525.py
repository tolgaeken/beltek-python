from random import randrange

liste = []

def rastgeleSayiEkle():
    for i in range(0,30):
        rndm = randrange(0,300)
        liste.append(rndm)
    
    print(liste)

    for i in liste:
        if(i%2==0):
            print(i)

rastgeleSayiEkle()

