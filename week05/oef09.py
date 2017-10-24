print("Geef de verschillende evaluatiecijfers door (sluit af met lege waarde)")
print("Uitmuntend: 5, Zeer goed: 4, Goed: 3, Voldoende: 2, Onvoldoende: 1, Zwak: 0")

database = {"0" : 0, "1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0}

score = input("Geef de nieuwe feedbackscore op: ")

while (score != ""):
    if (int(score) >= 0 and int(score) <= 5):
        database[score] += 1
    else:
        print("De ingegeven score ligt buiten de minimum of maximum waarde.")
    score = input("Geef de nieuwe feedbackscore op: ")

print("De gegevens zijn verwerkt. Dit is het resultaat:")
for key, value in database.items():
    print("Score: ", key, "-> Aantal: ", value)