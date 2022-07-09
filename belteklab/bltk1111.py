import bltk1111demo as demo

def calistir(cls,url):
    site = cls(url)
    fiyat = site.fiyatGetir()
    print(fiyat)

def main():
    calistir(demo.Hepsiburada,"https://www.hepsiburada.com/enjoy-tavuklu-yetiskin-kedi-mamasi-15-kg-p-PTLIENJ03")
    calistir(demo.Trendyol,"https://www.trendyol.com/enjoy/tavuklu-yetiskin-kedi-mamasi-15-kg-p-750051?boutiqueId=593321&merchantId=107493")
    calistir(demo.Amazon,"https://www.amazon.com.tr/Royal-Canin-Kitten-Yavru-Maması/dp/B000OLFXRU/ref=sr_1_4?__mk_tr_TR=ÅMÅŽÕÑ&keywords=kedi+maması&qid=1639654711&sr=8-4")

if __name__ == "__main__":
    main()