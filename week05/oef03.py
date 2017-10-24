nmct = {"1NMCT": 101, "2NMCT": 88, "3NMCT": 77}
devine = {"1Devine": 123, "2Devine": 98, "3Devine": 55}

print(nmct)

print(nmct.get("1NMCT"))

nmct["4NMCT"] = "Onbekend"
print(nmct)

nmct["1NMCT"] = "102"
print(nmct)

if "1Devine"in devine.keys():
    print("Key is aanwezig")
else:
    print("Key is niet aanwezig")

del(devine["2Devine"])
print(devine)

del(devine["2Devine"])
print(devine)