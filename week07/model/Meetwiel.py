import math

class Meetwiel:
    def __init__(self, _straal:float, _omwentelingen:int) -> None:
        self.straal = _straal
        self.omwentelingen = _omwentelingen

    @property
    def straal(self):
        return self.__straal

    @straal.setter
    def straal(self, value):
        self.__straal = value

    @property
    def omwentelingen(self):
        return self.__omwentelingen

    @omwentelingen.setter
    def omwentelingen(self, value):
        if (value == ""):
            self.__omwentelingen = 0
        else:
            self.__omwentelingen = value

    @property
    def omtrek(self):
        return 2 * self.__straal * math.pi

    @property
    def afstand(self):
        return self.__omwentelingen * self.omtrek

    def __str__(self) -> str:
        return "Meetwiel met straal {0} en omwentelingen {1}".format(self.straal, self.omwentelingen)

