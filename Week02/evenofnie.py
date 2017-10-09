getal = int(input("Geef een getal: "))

evenofnie = getal % 2

if (evenofnie != 0 or getal == 1):
    print("Het getal {0} is oneven".format(getal))
else:
    print("Het getal {0} is even".format(getal))