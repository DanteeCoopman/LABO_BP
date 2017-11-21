class Auto:
    def __init__(self, _kleur:str, _merk:str, _brandstof:str, _model:str, _kilometerstand:int) -> None:
        self.kleur = _kleur
        self.merk = _merk
        self.brandstof = _brandstof
        self.model = _model
        self.kilometerstand = _kilometerstand

    @property
    def kleur(self):
        return self.__kleur

    @kleur.setter
    def kleur(self, value):
        self.__kleur = value

    @property
    def kilometerstand(self):
        return self.__kilometerstand

    @kilometerstand.setter
    def kilometerstand(self, value):
        self.__kilometerstand = value

    @property
    def merk(self):
        return self.__merk

    @merk.setter
    def merk(self, value):
        self.__merk = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def brandstof(self):
        return self.__brandstof

    @brandstof.setter
    def brandstof(self, value):
        self.__brandstof = value

    def rijden(self, aantal_km):
        self.kilometerstand += aantal_km

    def __str__(self) -> str:
        return "merk {0} van model {1} met kleur {2}".format(self.merk, self.model, self.kleur )


