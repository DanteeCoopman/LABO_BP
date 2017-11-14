dictionary = {}

path = "tekstbestanden/scores.txt"

def inlezen_scores_studenten(bestandsnaam):
    fo = open(bestandsnaam)
    for line in fo:
       (key, value) = line.rstrip("\n").split(":",1)
       list = []
       value = value.split(':')
       for number in value:
           list.append(int(number))
       dictionary[key] = list
    fo.close()
    return(dictionary)

print(inlezen_scores_studenten(path))

naamdeel = input("Geef (een deel van) de naam an een student op: ")
naamdeel = naamdeel.title()

def print_scores(zoekwaarde):
    for key in dictionary:
        if key.startswith(zoekwaarde):
            print(key)
            print("De scores van deze student zijn: ", dictionary[key])
            print("De gemiddelde score is: ", sum(dictionary[key])/len(dictionary[key]))

print_scores(naamdeel)