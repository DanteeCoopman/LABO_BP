startwaarde = int(input("Geef een startwaarde op: "))
stapgrootte = int(input("Geef een positieve stapgrootte op: "))
hoeveelheid = int(input("Hoeveel getallen moeten er afgeprint worden? "))

def print_lijst_getallen(startwaarde, stapgrootte, hoeveelheid):
    for startwaarde in range(startwaarde, (stapgrootte*hoeveelheid)+startwaarde, stapgrootte):
        print(startwaarde)
        startwaarde += stapgrootte

print_lijst_getallen(startwaarde,stapgrootte,hoeveelheid)