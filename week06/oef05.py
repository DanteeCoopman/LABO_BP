morse_dictionary = {}

path = "tekstbestanden/MorseVertaling.txt"

def inlezen_morse_bestand(bestandsnaam):
    fo = open(bestandsnaam)
    for line in fo:
       (key, value) = line.rstrip("\n").split(";")
       morse_dictionary[key] = value
    fo.close()
    return(morse_dictionary)

print(inlezen_morse_bestand(path))

to_translate = input("Geef uw tekst in: ")

def vertaal_tekst_in_morse(te_vertalen_tekst):
    te_vertalen_tekst = te_vertalen_tekst.lower()
    vertaling = ""
    for letter in te_vertalen_tekst:
        vertaling += morse_dictionary[letter]
    return(vertaling)

print(vertaal_tekst_in_morse(to_translate))