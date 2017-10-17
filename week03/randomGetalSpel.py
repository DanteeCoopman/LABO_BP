from random import randint

getal = randint(0, 20)

geradengetal = int(input("Raad het getal: "))



while geradengetal != getal:
    if (geradengetal > getal):
        print("Lager")
        geradengetal = int(input("Raad het getal: "))
    elif(geradengetal < getal):
        print("Hoger")
        geradengetal = int(input("Raad het getal: "))
