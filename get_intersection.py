lst1 = [ 4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91] 
lst2 = [9, 9, 74, 21, 45, 11, 63] 
lst3 = []
def my_intersection(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if j == i:
                lst3.append(j)
            print(lst3)

#my_intersection(lst1, lst2)

def other_intersection(lst1, lst2):
    for i in lst2:
        if i in lst1:
            lst3.append(i)
            print(lst3)


#other_intersection(lst1, lst2)

def another_intersection(lst1, lst2):
    for i in lst1:
        if i in lst2 and i in lst1:
            lst3.append(i)
            print(lst3)

another_intersection(lst1, lst2)