meyve = ["elma","armut","muz"]
meyve.append("üzüm")
# print(len(meyve))

# for i in range(0,len(meyve)):
#     print(meyve[i])

# for i in meyve:
#     print(i)

notlar = [15,85,40,100,20,50,90,110]

for i in notlar:
    if(i >= 70 and i <=100):
        print("İyi")
    elif(i<70 and i >=0):
        print("Kötü")
    else:
        print("Hatalı Not")
    