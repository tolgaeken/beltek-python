zombiSayisi = int(input("Zombi sayısı girin"))

def zombiOldur():
    while True:
        global zombiSayisi
        if(zombiSayisi == 0):
            print("Zombi kalmadı")
            break

        elif (zombiSayisi>0):
            zombiSayisi-=1
            print(f"1 zombi öldürüldü kalan zombi sayısı : {zombiSayisi}")   

zombiOldur()