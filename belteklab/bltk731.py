ogrenciler = {
    1234: {
        "Adi":"Mehmet",
        "Soyadi":"Yıldırım",
        "Sinifi":1,
        "Şubesi":"B",
        "Ders Notları":{
            "Mat":78,
            "Fiz":84,
            "Alg":68
        }
    },
    2345: {
        "Adi":"Ayşe",
        "Soyadi":"Metin",
        "Sinifi":2,
        "Şubesi":"C",
        "Ders Notları":{
            "Mat":65,
            "Fiz":57,
            "Alg":91}
    },
    3456: {
            "Adi":"Mesut",
            "Soyadi":"Güneş",
            "Sinifi":1,
            "Şubesi":"B",
            "Ders Notları":{
                "Mat":47,
                "Fiz":61,
                "Alg":59
        }
    },
    4567: {
        "Adi":"Aylin",
        "Soyadi":"Tahtacı",
        "Sinifi":1,
        "Şubesi":"B",
        "Ders Notları":{
            "Mat":89,
            "Fiz":97,
            "Alg":93
        }
    },
    5678: {
        "Adi":"Murat",
        "Soyadi":"Kuru",
        "Sinifi":1,
        "Şubesi":"B",
        "Ders Notları":{
            "Mat":47,
            "Fiz":65,
            "Alg":87
        }
    },

}

def ortHesapla(dnotlari):
    i = 0
    for key,val in dnotlari.items():
        i+=val
    ort = i / len(dnotlari)
    return round(ort,2)

def enyuksekortalama(dnotlari):
    i = 0
    for key,val in dnotlari.items():
        if ortHesapla(dnotlari)>i:
            i = ortHesapla(dnotlari)
    
    return i


for key,val in ogrenciler.items():
    print(f"En yüksek ortalamaya sahip öğrenci : {val['Adi']} {val['Soyadi']} {enyuksekortalama(val['Ders Notları'])}")