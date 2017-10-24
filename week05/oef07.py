
test = {}

def geef_dict(dictionary):
    getal = 1
    while (getal <= 20):
        dictionary[getal] = getal * getal
        getal += 1
    print(dictionary)

geef_dict(test)

