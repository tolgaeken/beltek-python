def topla(*args):
    print(type(args))
    toplam = 0
    for i in args:
        toplam += i

    return toplam


print(topla(1,2,3,4,5,6))