gebruikersEenheid = input("Welke eenheid gebruikt u? [C: Celsius, F: Fahrenheit]")

def geef_celsius(t_in_fahrenheit):
    return(round((t_in_fahrenheit - 32) * 5/9, 2))

def geef_fahrenheit(temp_in_celsius):
    return(round((temp_in_celsius * 9/5) + 32, 2))

if (gebruikersEenheid == "C"):
    temp_in_celsius = float(input("Geef een temperatuur in Celsius op: "))
    print(geef_fahrenheit(temp_in_celsius))
elif (gebruikersEenheid == "F"):
    t_in_fahrenheit = float(input("Geef een temperatuur in Fahrenheit op: "))
    print(geef_celsius(t_in_fahrenheit))
else:
    print("Gelieve een correcte eenheid in te voeren.")


