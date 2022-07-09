while True:
    boy =  float(input("Boyunuzu giriniz (m cinsinden)\n"))
    kilo = int(input("Kilonuzu giriniz\n"))
    bmi = round(kilo/(boy**2),2)
    print(f"Kilonuz : {kilo} , Boyunuz : {boy} , BMI değeriniz {bmi}\n")