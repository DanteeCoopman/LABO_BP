class Winkelkar:
    def __init__(self) -> None:
        self.__productenlijst = []

    @property
    def productenlijst(self):
        return self.__productenlijst

    def voeg_toe(self, product):
        self.__productenlijst.append(product)

    def verwijder(self, product):
        self.__productenlijst.remove(product)

    def tel_op(self, winkelkar):
        self.__productenlijst = self.productenlijst + winkelkar.productenlijst




    def __str__(self) -> str:
        return super().__str__()


