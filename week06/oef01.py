def lees_en_nummer(bestandsnaam):
    fo = open(bestandsnaam)
    line = fo.readline()
    index = 1

    while(line):
        line = line.rstrip("\n")
        print("{0}:{1}".format(index, line))
        line = fo.readline()
        index += 1

    fo.close()

lees_en_nummer("tekstbestanden/tekstbestand.txt")