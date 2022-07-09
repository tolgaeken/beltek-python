import parola

parolalar = dict()

while True:
    site = input("Başlık giriniz:\t")

    if site == "ç":
        break

    url = input("URL'i giriniz:\t")
    kullanici_adi = input("Bir kullanıcı adı giriniz:\t")
    sifre = input("Bir parola giriniz, random üretmek için r yazınız")

    if sifre == "r":
        karakter_sayisi = int(input("Kaç karakterli bir parola istiyorsunuz?\t"))
        sifre = parola.parola_uret(karakter_sayisi)
        print("Yeni şifreniz:\t" + sifre)

    parolalar[site] = dict()
    parolalar[site]["URL"] = url
    parolalar[site]["kadi"] = kullanici_adi
    parolalar[site]["sifre"] = sifre



print(parolalar)