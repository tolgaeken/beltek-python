ayNo = int(input("""
Ay numarası giriniz
Ocak için 1
Şubat için 2
Mart için 3
Nisaniçin 4
Mayıs için 5
Haziran için 6
Temmuz için 7
Ağustos için 8
Eylül için 9
Ekim için 10
Kasım için 11
Aralık için 12\n"""))

if(ayNo<=12 and ayNo >=1):
    print(f"Seçilen ay için günlük ücret {ayNo*150} ₺ dir")
else:
    print("Hatalı bir ay seçimi yaptınız")



