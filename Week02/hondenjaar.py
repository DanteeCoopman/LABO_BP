hondenleeftijd = int(input("Geef de leeftijd van uw trouwe viervoeter in:  "))

mensenleeftijd = 22 + (hondenleeftijd - 2) * 5

if (hondenleeftijd <= 0):
    print("Dit is geen correcte leeftijd!")
elif (hondenleeftijd == 1):
    print("Deze leeftijd komt overeen met 14 mensenjaren.")
elif (hondenleeftijd == 2):
    print("Deze leeftijd komt overeen met 22 mensenjaren.")
else:
    print("Deze leeftijd komt overeen met {0} mensenjaren. ".format(mensenleeftijd))
