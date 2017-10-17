list1 = [78, 4, 5, 6, 4]
list2 = [4, 6, 5, 4, 78]

def geef_gemeenschappelijke_elementen(list1, list2):
    if (sorted(list1) == sorted(list2)):
        print("Deze lijsten hebben dezelfde elementen")
    else:
        print("Deze lijsten hebben niet dezelfde elementen")


geef_gemeenschappelijke_elementen(list1, list2)