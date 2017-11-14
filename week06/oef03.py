import os.path

path = "tekstbestanden/test2.txt"


def lees_en_nummer(bestandsnaam):
    fo = open(bestandsnaam)
    line = fo.readline()
    index = 1

    while (line):
        line = line.rstrip("\n")
        print("{0}: {1}".format(index, line))
        line = fo.readline()
        index += 1

    fo.close()

def schrijf_input_naar_bestand(bestandsnaam):
    fw = open(bestandsnaam, "w")
    while True:
        lijn = input("Geef een nieuwe lijn in of stop met s: ")
        if(lijn == "s"):
            break
        else:
            fw.write(lijn + "\n")
    fw.close()

def vul_bestand_aan(bestandsnaam):
    fw = open(bestandsnaam, "a")
    while True:
        lijn = input("Geef een nieuwe lijn in of stop met s: ")
        if(lijn == "s"):
            break
        else:
            fw.write(lijn + "\n")
    fw.close()

if os.path.isfile(path):
    vul_bestand_aan(path)
    lees_en_nummer(path)
else:
    schrijf_input_naar_bestand(path)