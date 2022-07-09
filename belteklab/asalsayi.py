nb = int(input("Kaça kadar asal sayılar bulunsun\n"))

print("\n")

for i in range(2,nb):
    for j in range (2,i):
        if(i%j==0):
            break
    else:
        print(i)