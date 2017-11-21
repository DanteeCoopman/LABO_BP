from model.Auto import Auto
import random

porsche = Auto("Zwart", "Porsche", "Benzine", "Panamera", 10000)
audi = Auto("Wit", "Audi", "Benzine", "A7", 3000)

autos = []

autos.append(porsche)
autos.append(audi)

for auto in autos:
    auto.rijden(random.randint(50, 850))
    print("de wagen {0} heeft {1} kilometers".format(auto.model, auto.kilometerstand))