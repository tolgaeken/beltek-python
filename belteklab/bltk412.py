dersNotuKatsayiListe= []
dersKredisiListe = []
i = 0
toplamDeger = 0
toplamkredi = 0

while True:
    dersNotu = input(f"{i+1}. Dersin harf notunu giriniz \n")

    if(dersNotu.lower() == "çıkış"):
        for j in range(0,len(dersNotuKatsayiListe)):
            toplamDeger = toplamDeger + dersNotuKatsayiListe[j]
            toplamkredi = toplamkredi + dersKredisiListe[j]
        sonuc = toplamDeger/(toplamkredi)
        print(sonuc)
        break

    dersKredisi = int(input(f"{i+1}. Dersin kredi puanı giriniz \n"))
    dersKredisiListe.append(dersKredisi)

    if(dersNotu.lower() == "aa"):
        dersNotuKatsayiListe.append(4.0*dersKredisi)
    elif(dersNotu.lower() == "ba"):
        dersNotuKatsayiListe.append(3.3*dersKredisi)
    elif(dersNotu.lower() == "bb"):
        dersNotuKatsayiListe.append(3.0*dersKredisi)
    elif(dersNotu.lower() == "cb"):
        dersNotuKatsayiListe.append(2.3*dersKredisi)
    elif(dersNotu.lower() == "cc"):
        dersNotuKatsayiListe.append(2.0*dersKredisi)
    elif(dersNotu.lower() == "dd"):
        dersNotuKatsayiListe.append(1.0*dersKredisi)
    else:
        print("Hatalı giriş")

    i+=1