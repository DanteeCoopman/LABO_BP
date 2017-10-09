import datetime

intMaand = int(input("Geef een maandnummer in:  "))

def functieMaand(intMaand):
    return(datetime.date(1900, intMaand, 1).strftime('%B'))



if (intMaand > 12 or intMaand < 1):
    print("Dit getal is foutief.")
else:
    print(functieMaand(intMaand))
