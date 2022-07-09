boy = int(input("Boyunuzu giriniz (cm cinsinden)\t"))
kilo = int(input("Kilonuzu giriniz\t"))
bki = round(kilo / ((boy**2)/10000),2) 
print(f"Boyunuz :\t{boy} \nKilonuz :\t{kilo}\nBKİ değeriniz :\t{bki}")