from tekrar import random_elemanli_list_uret

def son_eleman_sil_dondur(elements):
    temp = elements[-1]
    del elements[-1]
    return temp, elements

rand_listim = random_elemanli_list_uret(5, 0, 100)
print(rand_listim)

son_eleman, rand_listim = son_eleman_sil_dondur(rand_listim)

print(son_eleman)
print(rand_listim)