def toplama(*args):
    toplam = 0
    for i in args:
        toplam+=i

    return toplam

def cikarma(sayi1,sayi2):
    return sayi1-sayi2

def carp(*args):
    carpim = 1
    for i in args:
        carpim+=i

    return carpim

def bol(s1,s2):
    return s1/s2

def test(*sila):
    toplam = 0
    for i in sila:
        toplam+=i
    return toplam