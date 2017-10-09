import datetime
now = datetime.datetime.now()

geboortejaar = int(input("Geef je geboortejaar: "))

huidig = int(now.year)

if (huidig - geboortejaar >= 18):
    print("Ok, u mag alcohol drinken")
else:
    print("U bent nog geen 18! \n Kom volgend jaar terug...")