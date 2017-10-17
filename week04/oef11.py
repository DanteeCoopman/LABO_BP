list1 = [78, 4, 5, 6, 4]
list2 = [89, 78, 4]

def geef_gemeenschappelijke_elementen(list1, list2):
    print(set(list1)&set(list2))

geef_gemeenschappelijke_elementen(list1, list2)