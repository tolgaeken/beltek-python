with open ("bltk814gezegenler.txt","r") as f:
    fileContent = f.read()
    myList = fileContent.split("\n")

print(myList)


with open ("bltk814gezegenekleme.txt","a") as f:
    for i in myList:
        f.write(i + "\n")