geheleGetallen = [12, 45, -9, -15]
decimaleGetallen = [12.23, 45.1, 9.478, 15.125, -3.14]
verzamelingStrings = ["Stijn", "Lies", "Henk"]

def print_list(my_list_name, my_list):
    print(my_list_name)
    for element in my_list:
        print("Element {0} staat op index {1}".format(element, my_list.index(element)))


print_list("geheleGetallen", geheleGetallen)
print_list("decimaleGetallen", decimaleGetallen)
print_list("verzamelingStrings", verzamelingStrings)