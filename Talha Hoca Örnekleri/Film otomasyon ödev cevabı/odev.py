yetkili_ad = "admin"
yetkili_parola = "12345"

kullanici_adi = input("Kullanıcı adınızı girinzi:\t")
parola = input("Şifrenizi giriniz")

giris_deneme_counter = 0
while giris_deneme_counter < 3:
  if kullanici_adi == yetkili_ad and parola == yetkili_parola:
    break
  else:
    print("Kullanıcı adı ya da şifre hatalı, tekrar deneyin")
    kullanici_adi = input("Kullanıcı adınızı girinzi:\t")
    parola = input("Şifrenizi giriniz")
    giris_deneme_counter += 1
    if giris_deneme_counter == 3:
      raise SystemExit("Üçten fazla kez kullanıcı adı ya da şifre hatalı girildi, program durduruluyor.")

menu = """1.Film ekle
2. Filmleri listele
3. Film sil
4. Film bilgisi düzenle
5. Çıkış
"""

film_list = []
while True:
  print(menu)
  secenek = int(input("Lütfen seçenek numarasını giriniz:\t"))

  if secenek == 1:
    film_baslik = input("Film başlığı giriniz:\t")
    film_yonetmen = input("Filmin yönetmeninin adını giriniz:\t")
    film_oyuncular = []

    while True:
      oyuncu_ad = input("Bir oyuncu adı giriniz, çıkmak için ç yazınız:\t")
      if oyuncu_ad.lower() == "ç":
        break
      film_oyuncular.append(oyuncu_ad)

    film_dil = input("Lütfen filmin dilini giriniz:\t")
    izlenme_bilgisi = input("Filmi izlediyseniz e, izlemediyseniz h yazınız:\t")
    izlenme_bilgisi = izlenme_bilgisi.lower()

    if izlenme_bilgisi == "e":
      izlenme_bilgisi = True
    elif izlenme_bilgisi == "h":
      izlenme_bilgisi = False
    else:
      print("Yanlış bir seçenek girildi. Ana menüye dönülüyor.")
      continue

    film = [film_baslik, film_yonetmen, film_oyuncular, film_dil, izlenme_bilgisi]
    alt_secenek = input("Sıraya eklemek için 1'e sona eklemek için 2'ye basınız:\t")
    
    if alt_secenek == 1:
      film_list.append(film)
    elif alt_secenek == 2:
      index = int(input("Eklemek istediğiniz sıra numarasını giriniz."))-1
      if index < len(film_list):
        film_list.insert(index, film)
      else:
        print("Yanlış bir seçenek girildi. Ana menüye dönülüyor.")
      continue

    else:
      print("Yanlış bir seçenek girildi. Ana menüye dönülüyor.")
      continue
    
  elif secenek == 2:
    if len(film_list) <= 10:
      for index, film in enumerate(film_list):
        print(index+1, end=". ")
        for info in film:
          print(str(info), end=" ")
    else:
      baslangic = int(input("Lütfen başlangıç no girin:\t"))-1
      bitis = int(input("Lütfen bitis no girin:\t"))-1
      if baslangic < 0 or bitis >= len(film_list):
        print("İndis numaraları hatalı.")
        continue
      else:
        for i in range(baslangic,bitis):
          print(i+1, end=". ")
          for info in film_list[i]:
            print(str(info), end=" ")

  elif secenek == 3:
    silinecek_index = int(input("Silinecek filmin sıra numarasını giriniz:\t"))-1
    if silinecek_index < 0 or silinecek_index >= len(film_list):
      print("İndis numarası hatalı")
      continue
    temp_film = film_list[silinecek_index]

    for info in temp_film:
      print(str(info), end=" ")

    onay = input("Onaylıyor musunuz?(e ya da h):\t")
    if onay.lower() == "e":
      del film_list[silinecek_index]
    else:
      print("Silme işlemi başarısız.")
      continue

  elif secenek == 4:
    index = int(input("Güncellemek istediğiniz filmin indisini giriniz:\t"))-1
    if index < 0 or index >= len(film_list):
      continue 
    temp_fim = film_list[index]
    print(temp_film[0])
    film_ad = input("Yeni film adı giriniz")
    print(temp_film[1])
    yonetmen = input("Yeni yönetmen adı giriniz")
    print(str(temp_film[2]))
    temp_film[2] = []
    while True:
      oyuncu = input("Yeni oyuncu adı giriniz. Çıkmak için ç yazınız")
      if oyuncu.lower() == "ç":
        break
      temp_film[2].append(oyuncu)
    print(temp_film[3])
    temp_film[3] = input("Yeni film dili giriniz:\t")
    print(temp_film[4])
    izlenme = input("İzlediyseniz e izlemediyseniz h giriniz:\t").lower()
    if izlenme == "e":
      temp_film[4] = True
    elif izlenme == "h":
      temp_film[4] = False
    else:
      print("Yanlış bilgi verildi")
      continue
  elif secenek == 5:
    break
  else:
    print("Yanlış bir seçenek girdiniz.")
    continue

print("Program sonlandırıldı.")