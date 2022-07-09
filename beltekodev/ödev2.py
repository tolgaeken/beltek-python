aractipi = int(input("Araç tipi minibüs ise 1 e, panelvan ise 2 ye basınız\t"))
aracYas = int(input("Aracın yaşınız giriniz\t"))

if(aractipi == 1):
    if(aracYas <=6 and aracYas >= 1):
        mtvUcret = 523
    elif(aracYas <=15 and aracYas >= 7):
        mtvUcret = 346
    elif(aracYas >= 16):
        mtvUcret = 172
    print(f"{aracYas} yaşındaki bir minibüs için ödemeniz gereken miktar {mtvUcret} ₺")

elif(aractipi == 2):
    aracMotorHacmi = int(input("Aracon motor hacmini giriniz \t"))
    if(aracMotorHacmi < 1900):
        if(aracYas <=6 and aracYas >= 1):
            mtvUcret = 697
        elif(aracYas <=15 and aracYas >= 7):
            mtvUcret = 436
        elif(aracYas >= 16):
            mtvUcret = 260
    elif(aracMotorHacmi >= 1900):
        if(aracYas <=6 and aracYas >= 1):
            mtvUcret = 1052
        elif(aracYas <=15 and aracYas >= 7):
            mtvUcret = 697
        elif(aracYas >= 16):
            mtvUcret = 436
    print(f"{aracMotorHacmi} cm3 motor silindir hacimli {aracYas} yaşındaki bir panelvan için ödemeniz gereken miktar {mtvUcret} ₺")