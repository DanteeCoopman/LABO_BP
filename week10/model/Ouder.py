from model.Persoon import Persoon
from model.Student import Student

class Ouder(Persoon):
    def __init__(self, _naam, _voornaam, _geboortejaar=2016):
        super().__init__(_naam, _voornaam, _geboortejaar)
        self.__studenten = []

    def __str__(self) -> str:
        return "Ouder " + super().__str__()

    def voeg_student_toe(self, student):
        if not isinstance(student, Student):
            raise ValueError("Geen geldige student" + str(student))

        if not student in self.__studenten:
            self.__studenten.append(student)

    def geef_info_studenten(self):
        info_studenten = ""
        for student in self.__studenten:
            info_studenten += str(student) + "in opleiding " + student.opleiding + "\n"

        return info_studenten

    def geef_opleidingen_studenten(self):
        opleidingen = []
        for student in self.__studenten:
            opleidingen.append(student.opleiding)

        return opleidingen