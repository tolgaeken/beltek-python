girdi = input("Bir Sayı Giriniz\n")

try:
    girdi = int(input)
except:
    print("Bir Hata Oluştu")
finally:
    girdi = str(girdi)
    print(girdi)

## raise incelenecek