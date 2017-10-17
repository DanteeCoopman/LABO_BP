vrienden = []

naam = input("Geef de naam van een vriend op of sluit af met een leeg veld: ")

while (naam != ""):
    vrienden.append(naam)
    naam = input("Geef de naam van een vriend op of sluit af met een leeg veld: ")

print("Uw vrienden zijn:", vrienden)

