minlength = int(input("Geef de minimumlengte va, het paswoord op: "))
maxlength = int(input("Geef de maximumlengte va, het paswoord op: "))



if (minlength < maxlength):
    from random import randint
    paswoordlength = randint(minlength, maxlength)

    print("Gekozen lengte: {0}".format(paswoordlength))

    import random
    import string

    paswoord = ''.join([random.choice(string.ascii_letters) for n in range(paswoordlength)])

    print(paswoord)

else:
    print("Dit is geen geldige paswoordlengte!")

