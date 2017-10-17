maanden =['Januari', 'Februari', 'Maart', 'April', 'Mei', 'Juni', 'Juli', 'Augustus', 'September', 'Oktober', 'November', 'December']
getallen = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

def kies_element(maanden, getallen):
    import random
    print("De gekozen maand is", random.choice(maanden))
    print("Het gekozen getal is", random.choice(getallen))

kies_element(maanden, getallen)