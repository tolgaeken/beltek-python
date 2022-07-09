sayilar = [10,20,40,50,60]

sayilar2 = sayilar[2:5]
for i in sayilar2:
    print(i)

print("-------")

sayilar3 = sayilar[-1]
print(sayilar3)

print("-------")

sayilar4 = sayilar[::-1]
for i in sayilar4:
    print(i)

print("-------")

sayilar.insert(2,30)
for i,j in enumerate(sayilar):
    print(i)

print("-------")

sayilar.insert(2,[30,31,32,33])
for i,j in enumerate(sayilar):
    print(i)

print(sayilar)