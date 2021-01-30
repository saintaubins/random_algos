

from collections import Counter


#remove duplucates from a list

# l = [1,2,3,4,1,2]
# def remove_duplicates(l):
#     l = list(dict.fromkeys(l))
#     print(l)
# remove_duplicates(l)

# initializing list 
#test_list = [1, 4, 5, 8, 10] 
  
# printing original list  
#print ("Original list : " + str(test_list)) 
  
# using naive method to  
# check sorted list  
#flag = 0
#i = 1
#while i < len(test_list): 
    #if(test_list[i] < test_list[i - 1]): 
        #flag = 1
    #i += 1
      
# printing result 
#if (not flag) : 
    #print ("Yes, List is sorted.") 
#else : 
    #print ("No, List is not sorted.") 


# test_list = [1, 3, 5, 6, 3, 5, 6, 1, 1] 
# print ("The original list is : " +  str(test_list)) 

# res = [] 
# for i in test_list: 
#     if i not in res: 
#         res.append(i)

# print ("The list after removing duplicates : " + str(res)) 


#convert a list to a dictionary

#lst = ['a', 1, 'b', 2, 'c', 3, 'e', 9, 'cat', 12]

# def Convert(lst):
#     my_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
#     return my_dct

# print(Convert(lst))


#count the amount of occurrences in a list
#method 1

# a_list = ["a", "b", "a"]

# occurrences = a_list.count("a")

# print(occurrences)

#method 2

#a_list = ["a", "b", "a"]

list1 = ['x','y','z','x','x','x','y', 'z']

#my_str = "Welcome to Sem's Sandbox!"

#dict1 = {'x': 4, 'y': 2, 'z': 2, 'z': 2}

#tuple1 = ('x','y','z','x','x','x','y','z')

occurrences = Counter(list1)

print(occurrences)

