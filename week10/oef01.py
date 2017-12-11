from model.Student import Student
from model.Ouder import Ouder

def testOuder():
    student1 = Student("Naam1", "Voornaam1", 199001, "NMCT", 1990)
    student2 = Student("Naam2", "Voornaam2", 199002, "NMCT", 1990)
    student3 = Student("Naam3", "Voornaam3", 199003, "NMCT", 1990)

    ouder1 = Ouder("Oudernaam1", "Oudervoornaam1", 1970)

    ouder1.voeg_student_toe(student1)
    ouder1.voeg_student_toe(student2)
    ouder1.voeg_student_toe(student3)

    print(ouder1.geef_info_studenten())

    print(ouder1)




testOuder()