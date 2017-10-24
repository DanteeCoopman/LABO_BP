nmct = {"1NMCT": 101, "2NMCT": 88, "3NMCT": 77}
devine = {"1Devine": 123, "2Devine": 98, "3Devine": 55}

howest = {**nmct, **devine}


key = input("Geef uw key: ")
value = input("Geef uw value: ")

def voeg_nieuw_element_toe(key):
    if key in howest.keys():
        print("Toevoegen mislukt. Key '{0}' is reeds aanwezig. ".format(key))
    else:
        howest[key] = value

def print_dictionary(name, dictionary):
    print("Dictionary: {0}".format(name))
    for key, value in dictionary.items():
        print("Key: ", key, "-> Value: ", value)


voeg_nieuw_element_toe(key)
print_dictionary("Howest", howest)
