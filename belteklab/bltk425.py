kitapListe = []

i=0

while True:
    
    menu = int(input("""\tKitap eklemek için 1'e
    Mevcut sıranın içine kitap eklemek için 2'ye basınız
    Çıkış yapmak için 3'e basınız
    \n"""))

    if(menu==1):
        kitapAdi = input("Kitap adı giriniz\n")
        kitapYazar = input("Kitap yazarı giriniz\n")
        temp = [kitapAdi,kitapYazar]
        kitapListe.append(temp)
        i+=1
    
    elif(menu==2):
        for i,kitap in enumerate(kitapListe):
            print((i+1),",".join(kitap), end="*\n")
        
        ekleKitap = int(input("Eklemek istediğiniz kitabın numarasını giriniz\n"))-1

        if(ekleKitap>len(kitapListe)):
            print("Belirli kitap sayısının üstünde bir numara girdiniz\n")
            continue

        kitapAdi2 = input("Eklemek istediğiniz kitap adı giriniz\n")
        kitapYazar2 = input("Eklemek istediğiniz kitap yazarı giriniz\n")
        temp2 = [kitapAdi2,kitapYazar2]
        kitapListe.insert(ekleKitap,temp2)

    elif(menu==3):
        break

    else:
        print("Hatalı giriş yapıldı")
