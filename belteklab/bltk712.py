import random
import string

# string.ascii_letters
# string.digits
# string.punctuation
# random.choice(string.ascii_letters)


karakterler = string.ascii_letters+string.digits+string.punctuation


def parolauret(karakterUzunluk):
    parola =""
    for i in range(karakterUzunluk):
        parola+=random.choice(karakterler)
    
    print(parola)


parolauret(20)