# eski tip dosya açma

# full = "C:\\dev\\FilePath\\deneme.txt"
# relative = "FilePath\\deneme.txt"

f = open("FilePath\\deneme.txt","w")
f.write("Tlg\nTlg")
f.close


#yeni tip dosya açma

with open("FilePath\\test.py" ,"w") as f:
    f.write("Merhaba \n")