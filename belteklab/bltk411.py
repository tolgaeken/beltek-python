sayi = int(input("Hedeflenen sayıyı giriniz\n"))

for i in range(0,sayi):
    if(i%2==1):
        print(i)

for i in range(1,sayi,2):
    print(i)