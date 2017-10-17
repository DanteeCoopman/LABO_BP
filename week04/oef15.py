min = int(input("Geef een minimum waarde: "))
max = int(input("Geef een maximum waarde: "))

def kies_5_getallen(min,max):
    if (min >= max or (max - min) < 5):
        print("Met de ingegeven waarden kan geen berekening gemaakt worden!")
    else:
        import random
        print(random.sample(range(min, max), 5))

kies_5_getallen(min,max)