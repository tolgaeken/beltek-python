pi = 3.14

def topla(*args):
    sonuc = 0

    for element in args:
        sonuc += element

    return sonuc

def cikar(*args):
    sonuc = args[0]

    for index in range(1, len(args)):
        sonuc -= args[index]

    return sonuc

def carp(*carp):
    sonuc = 1

    for element in carp:
        sonuc *= element

    return sonuc

def bol(*bol):
    sonuc = bol[0]

    for index in range(1, len(bol)):
        sonuc /= bol[index]

    return sonuc