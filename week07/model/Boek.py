#Boek.py
class Boek:
    def __init__(self, _titel:str, _uitgeverij:int, _isbn:int, _jaar:int =2017) -> None:
        self.titel = _titel
        self.uitgeverij = _uitgeverij
        self.isbn = _isbn
        self.jaar = _jaar

    #properties (getter & setter)

    @property
    def titel(self):
        return self.__titel

    @titel.setter
    def titel(self, value):
        self.__titel  = value
    @property
    def uitgeverij(self):
        return self.__uitgeverij

    @uitgeverij.setter
    def uitgeverij(self, value):
        self.__uitgeverij = value

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, value):
        self.__isbn = value

    @property
    def jaar(self):
        return self.__jaar

    @jaar.setter
    def jaar(self, value):
        if (value > 2017):
            value = 2017
            print("Je maakte een fout")
        self.__jaar = value

    def doeIets(self):
        print(self.__jaar)

    def __str__(self) -> str:
        return super().__str__()