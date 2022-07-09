import string

girdi = input("Birşeyler giriniz\n")

def harfleriSay(karakterler):
    if (len(karakterler)==0):
        print("Hiçbirşey girilmedi")
        return

    k=0
    b=0

    for i in karakterler:
        if(i in string.ascii_uppercase):
            b+=1
        elif(i in string.ascii_lowercase):
            k+=1

    print(f"{b} adet büyük,{k} adet küçük harf vardır")

harfleriSay(girdi)