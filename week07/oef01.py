from model.Boek import Boek

boek1 = Boek("een titel", "Uitgeverijtje", 1236,2014)
boek2 = Boek("dinges", "danteeUItgeverij", 61865, 3000)

print(boek1.titel)
boek2.jaar = 2000
print(str(boek2.isbn) + "jaar" + str(boek2.jaar))
boek2.doeIets()