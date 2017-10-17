nieuwe_list_getallen = []

getal = 1

for getal in range(0,485,13):
    nieuwe_list_getallen.append(getal)
    getal += 13

print(nieuwe_list_getallen)

print(nieuwe_list_getallen[::-1])

del(nieuwe_list_getallen[0])
print(nieuwe_list_getallen)

print(nieuwe_list_getallen[-1])