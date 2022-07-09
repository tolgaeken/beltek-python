def ucretHesapla(saatlikUcret,calismaSuresi):

    if calismaSuresi>40:
        return (((calismaSuresi-40)*1.5)*saatlikucret) + (40*saatlikUcret)

    elif (calismaSuresi>=0 and calismaSuresi<=40):
        return calismaSuresi*saatlikucret
        