kenar_1 = int(input("1.Kenarını giriniz\n"))
kenar_2 = int(input("2. Kenarı Giriniz\n"))

def dikdortgenHesapla(kenar1,kenar2):
    return kenar1*kenar2

print(f"Dikdörtgenin alanı : {dikdortgenHesapla(kenar_1,kenar_2)}")