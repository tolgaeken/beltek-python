from math import pi

daireYaricapi = int(input("Dairenin yarıçapını giriniz\n"))

def daireYaricapiHesapla(yaricap):
    return round((pi*(yaricap**2)),2)

print(f"Dairenin alanı : {daireYaricapiHesapla(daireYaricapi)}")