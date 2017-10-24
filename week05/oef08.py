zin = input("Geef een zin in: ")

def tel_voorkomen_woorden(woorden):
    teller = dict()
    woorden = zin.split()

    for woord in woorden:
        if woord in teller:
            teller[woord] += 1
        else:
            teller[woord] = 1

    print("Dictionary: Woorden_dic")
    for key, value in teller.items():
        print("Key: ", key, "-> Value: ", value)


tel_voorkomen_woorden(zin)