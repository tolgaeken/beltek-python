import kaziyici


def main():
    hb = kaziyici.Hepsiburada("https://www.hepsiburada.com/royal-canin-sterilised-37-kisirlastirilmis-kuru-kedi-mamasi-15-kg-p-HBCV00000D0985")
    fiyat = hb.fiyat_getir()
    print(fiyat)


if __name__ == '__main__':
    main()
