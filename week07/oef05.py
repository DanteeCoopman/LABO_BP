from model.Winkelkar import Winkelkar

winkelkar1 = Winkelkar()
winkelkar2 = Winkelkar()
winkelkar3 = Winkelkar()

winkelkar1.voeg_toe("test")
winkelkar1.voeg_toe("test2")
winkelkar1.voeg_toe("test3")

print(winkelkar1.productenlijst)

winkelkar2.voeg_toe("test4")
winkelkar2.voeg_toe("test5")
winkelkar2.voeg_toe("test6")

winkelkar3 = winkelkar1.productenlijst + winkelkar2.productenlijst

winkelkar1.tel_op(winkelkar2)


print(winkelkar3)
print(winkelkar1.productenlijst)
