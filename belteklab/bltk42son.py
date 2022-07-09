kitapListe = []

i=0

while True:
    
    menu = int(input("Kitap eklemek için 1'e\nKitapları listelemek için 2'ye\nKitap düzenlemek veya silmek için 3'e\nÇıkış yapmak için 4'e basınız\n"))
    print("\n")

    if(menu==1):

        altMenu1 = int(input("Kitap eklemek için 1'e\nMevcut sıranın içine kitap eklemek için 2'ye basınız\nProgramdan çıkış yapmak için 3'e \nAna menüye dönmek için 4'e basınız\n"))
        print("\n")

        if(altMenu1==3):
            break

        elif(altMenu1==4):
            continue

        kitapAdi = input("Kitap adı giriniz\n")
        kitapYazar = input("Kitap yazarı giriniz\n")
        temp = [kitapAdi,kitapYazar]

        if(altMenu1==1):
            kitapListe.append(temp)
            i+=1
    
        elif(altMenu1==2):
            
            for i,kitap in enumerate(kitapListe):
                print((i+1),",".join(kitap), end="*\n\n")
            
            ekleKitap = int(input("Eklemek istediğiniz kitabın numarasını giriniz\n"))-1

            if(len(kitapListe)<ekleKitap):
                print(f"{len(kitapListe)} adet kitap vardır {ekleKitap+1} numaralı kitap geçersizdir\n")
                continue

            kitapListe.insert(ekleKitap,temp)

        else:
            print("Hatalı giriş yapıldı\n")

    elif(menu==2):

        if(len(kitapListe)==0):
            print("Mevcut bir kitap bulunmamaktadır\n")
            continue

        for i,kitap in enumerate(kitapListe):
            print((i+1),",".join(kitap), end="*\n\n")
    
    
    elif(menu==3):

        if(len(kitapListe)==0):
            print("Mevcut bir kitap bulunmamaktadır\n")
            continue

        for i,kitap in enumerate(kitapListe):
            print((i+1),",".join(kitap), end="*\n\n")

        altMenu2 = int(input("Kitap düzenlemek için 1'e\nKitap silmek için 2'ye basınız\nProgramdan çıkış yapmak için 3'e\nAna menüye dönmek için 4'e basınız\n"))
        print("\n")

        if(altMenu2 == 1):
           
            kitapNo = int(input("Düzenlemek istediğiniz kitap numarasını giriniz\n"))-1

            if(len(kitapListe)<kitapNo):
                print(f"{len(kitapListe)} adet kitap vardır {kitapNo+1} numaralı kitap geçersizdir\n")
                continue

            temp2 = kitapListe[kitapNo]
            print(f"Eski Kitap Adı : {temp2[0]}")
            temp2[0] = input("Yeni Kitap Adı Giriniz\n")
            print(f"Eski Yazar Adı : {temp2[1]}")
            temp2[1] = input("Yeni Yazar Adı Giriniz\n")

            kitapListe[kitapNo] = temp2


        elif(altMenu2 == 2):

            silKitap = int(input("Silmek istediğiniz kitabın numarasını giriniz\n"))-1

            if(len(kitapListe)<silKitap):
                print(f"{len(kitapListe)} adet kitap vardır {silKitap+1} numaralı kitap geçersizdir\n")
                continue
        
            del kitapListe[silKitap]

        elif(altMenu2 == 3):
            break

        elif(altMenu2 == 4):
            continue

        else:
            print("Hatalı giriş yapıldı\n")
            continue

    elif(menu==4):
        continue

    else:
        print("Hatalı giriş yapıldı\n")