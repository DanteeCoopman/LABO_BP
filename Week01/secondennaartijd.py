seconden = float(input("Seconden: "))

dagen = int(seconden/86400)

uren = int((seconden - (dagen * 86400))/3600)

minuten = int((seconden - (dagen * 86400) - (uren * 3600))/60)

overigeseconden = int(seconden - (dagen * 86400) - (uren * 3600) - (minuten * 60))

print(dagen,":", uren, ":", minuten, ":", overigeseconden)


