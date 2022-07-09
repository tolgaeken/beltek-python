import string
import random

def parola_uret(uzunluk):
    parola = ""
    base = string.ascii_letters + string.digits + string.punctuation

    for i in range(uzunluk):
        rastgele_deger = random.choice(base)
        parola += rastgele_deger

    return parola    