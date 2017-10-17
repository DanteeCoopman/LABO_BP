list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]

def zijn_verschillend(list1, list2):
    if(set(list1) == set(list2)):
        print("False")
    else:
        print("True")

zijn_verschillend(list1, list2)