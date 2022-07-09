import random
import string

# print(string.ascii_letters)
# print(string.digits) 
# print(string.punctuation)

# print(random.choice(string.ascii_letters))

def parola_uret(uzunluk):
    karakter_havuzu = string.ascii_letters + string.digits + string.punctuation
    parola = ""
    for i in range(uzunluk):
        parola += random.choice(karakter_havuzu)
    
    return parola

parolam = parola_uret(20)
print(parolam)
print(len(parolam))