def something(s):
    my_str = ''
    for i in s:
        my_str = i + my_str 

    return my_str


def palindrome(s):
    p = something(s)
    if p == s:
        print('is palaindrome')
    else:
        print('not palindrom muther fucker')

s = 'what the fuck'
palindrome(s)

def revarray(a):
    rev_a = a[::-1]
    
    print(rev_a)

a = [1,2,3,4]

def rev_array(a):
    rev_a = []
    i = -1
    count = 1
    while(count <= len(a)):
        rev_a.append(a[i])
        i -= 1
        count += 1
    print(rev_a)

revarray(a)
rev_array(a)

def rev_string(s):
    my_str = ''
    i = -1
    count = 1
    while(count <= len(s)):
        my_str += s[i]
        i -= 1
        count += 1
    print(my_str)

rev_string(s)

def remove_dups(ar):
    my_ar = []
    for i in ar:
        if i not in my_ar:
            my_ar.append(i)
    
    print(my_ar)
ar = [1,'what',2,2,'what','the','the','fuck',3,3]

remove_dups(ar)

tda = [
    ['joe', 'enter'],['joe', 'enter'],['joe', 'exit'],['joe', 'exit'],
    ['sally','exit'],['bob', 'exit'],['bob', 'enter'],['bob', 'exit'],
    ['bob','enter'],['bob', 'exit'],['sem', 'enter'],['sem', 'exit']]

def two_d_shit(tda):
    # violator, or good nigga
    exit_array = []
    enter_array = []
    name_array = []
    i = 0
    for name , action in tda:
        if name not in name_array:
            name_array.append(name)
    print('\nchecking for violators and such... \n')
    print('name array:',name_array,'\n')

    while i < len(name_array):
        for name, action in tda:
            if name == name_array[i] and action == 'enter':
                enter_array.append([name, action])
            if name == name_array[i] and action == 'exit':
                exit_array.append([name, action])

        if len(enter_array) != len(exit_array):
            print( name_array[i], 'is a violator','\n')
        else:
            print( name_array[i], 'is a good nigga','\n')

        print('enter_array:',enter_array,'\n' 'exit_array: ',exit_array,'\n')
        exit_array = []
        enter_array = []
        i += 1
    print('Peace yall...\n')
two_d_shit(tda)

a_arr = [1,2,2,3,3,3,3,4,4,4,'biyach',5]


def count_amount_func(count_amount_array):
    print('\ncounting the amount of occurances, of different types, in an array\n')
    print('\noriginal array:\n',a_arr,'\n')
    arr_types = []
    singles_array = []
    doubles_array = []
    triples_array = []
    quads_array = []

    for i in count_amount_array:
        if i not in arr_types:
            arr_types.append(i)
    print('arr_types: ',arr_types)

    for i in count_amount_array:
      
        if count_amount_array.count(i) == 1:
            singles_array.append(i) 
        if count_amount_array.count(i) == 2:
            doubles_array.append(i) 
        if count_amount_array.count(i) == 3:
            triples_array.append(i) 
        if count_amount_array.count(i) == 4:
            quads_array.append(i) 
    print('singles_array: ',singles_array,'\ndoubles_array: ',doubles_array,'\ntriples_array: ',triples_array,'\nquads_array:   ',quads_array)

count_amount_func(a_arr)

nums = [1, 3, 5, 6, 7, 9]
my_sum = 0
for num in nums:
    my_sum = my_sum + num
print('my_sum : ',my_sum)

my_dict = {
    'name': 'sem',
    'age': 25,
    'sex': 'male',
    'address': {
        'street': '117 Martens Ave',
        'city': 'Valley Stream',
        'state': 'New York',
        'zip': 11580
    }
}
for key, value in my_dict.items():
    if key == 'address':
        print('address:\n',value['street'],'\n',value['city'],value['state'],'\n',value['zip'])
    else:
        print('key:',key, 'value:',value)


