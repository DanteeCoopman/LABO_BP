nmct = {"1NMCT": 101, "2NMCT": 88, "3NMCT": 77}
devine = {"1Devine": 123, "2Devine": 98, "3Devine": 55}

def print_dictionary(name, dictionary):
    print("Dictionary: {0}".format(name))
    for key, value in dictionary.items():
        print("Key: ", key, "-> Value: ", value)

print_dictionary("NMCT", nmct)
print_dictionary("Devine", devine)