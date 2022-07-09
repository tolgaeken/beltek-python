kullaniciAdi = "admin"
parola = "adminparola"

filmListe = []
filmOyunculari = []

kullaniciGiris = input("Kullanıcı Adı Giriniz\n")
parolaGiris = input("Parola Giriniz\n")

# kullaniciGiris = "admin"
# parolaGiris = "adminparola"

if(kullaniciGiris.lower()== kullaniciAdi and parolaGiris.lower()==parola):
    print("Giriş Başarılı\n")
    while True:
        menu = int(input("1 - Film Ekle\n2 - Filmleri Listele\n3 - Film Sil\n4 - Film Bilgisi Düzenle\n5 - Çıkış\n"))

        if(menu==1):
            altMenu = int(input("1 - Listenin Sonuna Ekle\n2 - Listede Verilen Sıraya Ekle\n3 - Ana Menüye Dön\n4 - Çıkış\n"))
            
            if(altMenu==3):
                continue

            elif(altMenu==4):
                break

            filmAdi = input("Film Adı Giriniz\n")
            filmYonetmeni = input("Film Yönetmenini giriniz\n")
            
            while True:
                filmOyuncuGir = input("Film Oyuncularını giriniz.Oyuncular bitti ise 'bitti' yazınız\n")
                if(filmOyuncuGir.lower()=="bitti"):
                    break
                else:
                    filmOyunculari.append(filmOyuncuGir)
            
            filmOyunculari = str(filmOyunculari)
            filmDili = input("Filmin Dilini Giriniz\n")
            filmIzlendimi = input("Filmin izlendi ise 'evet' izlenmedi ise 'hayır' giriniz\n")
            if(filmIzlendimi.lower()=="evet"):
                filmDurumu = True
                filmDurumu = str(filmDurumu)
            elif(filmIzlendimi.lower()=="hayır"):
                filmDurumu = False
                filmDurumu = str(filmDurumu)
            else:
                print("Hatalı Giriş")
                continue
            
            temp = [filmAdi,filmYonetmeni,filmOyunculari,filmDili,filmDurumu]

            if(altMenu==1):
                filmListe.append(temp)
                filmOyunculari = []
            
            elif(altMenu == 2):
                if(len(filmListe)==0):
                    print("Mevcut bir film bulunmamaktadır.Listenin başına eklenecektir\n")
                    filmListe.append(temp)
                    filmOyunculari = []
                

                else:
                    ekleFilm = int(input("Eklemek istediğiniz filmin numarasını giriniz\n"))-1

                    if(len(filmListe)<ekleFilm):
                        print(f"{len(filmListe)} adet film vardır {ekleFilm+1} numaralı film geçersizdir\n")
                        continue

                    filmListe.insert(ekleFilm,temp)
                    filmOyunculari = []

        if(menu==2):
            if(len(filmListe)==0):
                print("Mevcut bir film bulunmamaktadır\n")
                continue

            if(len(filmListe)<=10):
                for i,film in enumerate(filmListe):
                    print((i+1),",".join(film), end="\n\n")
            
            elif (len(filmListe)>10):
                print("Film sayısı 10 dan fazladır. Filmlerin başlangıc ve bitiş sıra numarasını girmeniz gerekir\n")
                filmListeBaslangic = int(input("Başlangıç numarası giriniz\n"))-1
                filmListeBitis = int(input("Bitiş numaraşı giriniz\n"))-1

                for i,film in enumerate(filmListe[filmListeBaslangic:filmListeBitis+1]):
                    print((i+1),",".join(film), end="\n\n")


        if(menu==3):
            if(len(filmListe)==0):
                print("Mevcut bir film bulunmamaktadır\n")
                continue

            for i,film in enumerate(filmListe):
                print((i+1),",".join(film), end="\n\n")

            silFilm = int(input("Silmek istediğiniz filmin numarasını giriniz\n"))-1

            if(len(filmListe)<silFilm):
                print(f"{len(filmListe)} adet film vardır {silFilm+1} numaralı film geçersizdir\n")
                continue
            
            silFilmOnay = input(f"{silFilm+1} numaralı {filmListe[silFilm][0]} filmini silmek istediğinize emin misiniz?\n")

            if(silFilmOnay.lower() == "e"):
                del filmListe[silFilm]
                print("Film silindi...\n")
        
        if(menu==4):
            if(len(filmListe)==0):
                print("Mevcut bir film bulunmamaktadır\n")
                continue

            for i,film in enumerate(filmListe):
                print((i+1),",".join(film), end="\n\n")

            filmNo = int(input("Düzenlemek istediğiniz film numarasını giriniz\n"))-1

            if(len(filmListe)<filmNo):
                print(f"{len(filmListe)} adet film vardır {filmNo+1} numaralı film geçersizdir\n")
                continue

            temp2 = filmListe[filmNo]

            filmDuzenlenecekBilgi = int(input("Düzenlemek istediğiniz bilgiyi seçiniz\n1 - Film Adı\n2 - Film Yönetmeni\n3 - Film Oyuncuları\n4 - Film Dili\n5 - Film İzlenme Durumu\n"))

            if(filmDuzenlenecekBilgi==1):
                print(f"Eski Film Adı : {temp2[0]}")
                temp2[0] = input("Yeni Film Adı Giriniz\n")
                filmListe[filmNo] = temp2

            elif(filmDuzenlenecekBilgi==2):
                print(f"Eski Film Yönetmeni : {temp2[1]}")
                temp2[1] = input("Yeni Film Yönetmeni Giriniz\n")
                filmListe[filmNo] = temp2

            elif(filmDuzenlenecekBilgi==3):
                print(f"Eski Film Oyuncuları : {temp2[2]}")
                filmOyunculari = []
                while True:
                    filmOyuncuGir = input("Film Oyuncularını giriniz.Oyuncular bitti ise 'bitti' yazınız\n")
                    if(filmOyuncuGir.lower()=="bitti"):
                        break
                    else:
                        filmOyunculari.append(filmOyuncuGir)
                temp2[2] = str(filmOyunculari)
                filmListe[filmNo] = temp2


            elif(filmDuzenlenecekBilgi==4):
                print(f"Eski Film Dili : {temp2[3]}")
                temp2[3] = input("Yeni Film Dili Giriniz\n")
                filmListe[filmNo] = temp2

            elif(filmDuzenlenecekBilgi==5):
                print(f"Eski Film İzlenme Durumu : {temp2[4]}")
                filmIzlendimi = input("Filmin izlendi ise 'evet' izlenmedi ise 'hayır' giriniz\n")
                if(filmIzlendimi.lower()=="evet"):
                    temp2[4] = True
                    temp2[4] = str(temp2[4])
                elif(filmIzlendimi.lower()=="hayır"):
                    temp2[4] = False
                    temp2[4] = str(temp2[4])
                else:
                    print("Hatalı Giriş")
                    continue

            else:
                print("Hatalı Giriş")
                continue


        if(menu==5):
            break
        
else:
    print("Kullanıcı Adı veya Şifre Hatalıdır\n")