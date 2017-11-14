import random

path = "tekstbestanden/spelers.txt"
pathnieuw = "tekstbestanden/opstelling.txt"

def inlezen_spelers(bestandsnaam, nieuwbestand):
    fo = open(bestandsnaam)
    selectie = random.sample(fo.readlines(),11)
    fo.close()

    fw = open(nieuwbestand, "w")
    for spelers in selectie:
        fw.write(spelers)
    fw.close()

    fo = open(nieuwbestand)
    line = fo.readline()
    index = 1

    while (line):
        line = line.rstrip("\n")
        print("{0}: {1}".format(index, line))
        line = fo.readline()
        index += 1

    fo.close()


inlezen_spelers(path, pathnieuw)