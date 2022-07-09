kisiListe = []

while True:
    kisiAd = input("Kişi adı giriniz, çıkış yapmak için çıkış yazınız\n")

    if(kisiAd.lower() == "çıkış"):
        break

    kisiSoyad = input("Kişi soyadı giriniz\n")
    kisiTelefon = input("Kişinin telefonunu giriniz\n")
    kisiMail = input("Kişinin Mail Adresini giriniz\n")

    temp = [kisiAd,kisiSoyad,kisiTelefon,kisiMail]

    kisiListe.append(temp)

for kisi in kisiListe:
    print(",".join(kisi),end="*\n")