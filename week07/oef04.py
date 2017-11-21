from model.Meetwiel import Meetwiel

meetwiel1 = Meetwiel(0.9, "")

print(meetwiel1)

vermeerder = 0

while (vermeerder != "c"):
    vermeerder = input("Geef het aantal extra omwentelingen door: ")
    if(vermeerder != "c" ):
        meetwiel1.omwentelingen += int(vermeerder)

print(meetwiel1)

print("Meetwiel legde {0}m af".format(round(meetwiel1.afstand, 2)))

