kisiler = {
    "kisi1" : {
        "Adi" : "Ali",
        "Soyadi" : "Yildirim",
        "Yas" : 21
    },
    "kisi2" : {
        "Adi" :"Huseyin",
        "Soyadi" : "Mutlu" ,
        "Yas" : 33
    }
}

for k,v in kisiler.items():
    print(f"Kişi No : {k}")
    for k2,v2 in v.items():
        print(f"\t\t{k2}\t\t{v2}")