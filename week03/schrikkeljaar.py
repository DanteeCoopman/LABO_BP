startjaar = int(input("Geef een jaartal om te starten op: "))
stopjaar = int(input("Geef een jaartal om te stoppen op: "))

if(stopjaar - startjaar <= 0):
    print("Het startjaar moet lager zijn dan het stopjaar!")
else:
    while startjaar < stopjaar + 1:
        if (startjaar % 4 == 0 and startjaar % 100 != 0 ):
            print(startjaar)
        elif (startjaar % 400 == 0):
            print(startjaar)
        startjaar += 1
