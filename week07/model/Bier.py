class Bier:
    def __init__(self, _naam:str, _brouwerij:str, _kleur:str, _alcohol:float) -> None:
        self.naam = _naam
        self.brouwerij = _brouwerij
        self.kleur = _kleur
        self.alcohol = _alcohol

    @property
    def naam(self):
        return self.__naam

    @naam.setter
    def naam(self, value):
        if (value != ""):
            self.__naam = value
        else:
            self.__naam = "Onbekend"

    @property
    def brouwerij(self):
        return self.__brouwerij

    @brouwerij.setter
    def brouwerij(self, value):
        self.__brouwerij = value

    @property
    def alcohol(self):
        return self.__alcohol

    @alcohol.setter
    def alcohol(self, value):
        if (value <= 100 and value >= 0):
            self.__alcohol = value
        else:
            self.__alcohol = "Ongeldige waarde"


    def __str__(self) -> str:
        return super().__str__()