string1 = input("Geef een woord:")
string2 = input("Geef nog een woord:")

tweeLettersVanString1 = string1[:2]

tweeLettersVanString2 = string2[:2]

combinedString1 = tweeLettersVanString2 + string1[2:]
combinedString2 = tweeLettersVanString1 + string2[2:]


print(combinedString1)
print(combinedString2)


