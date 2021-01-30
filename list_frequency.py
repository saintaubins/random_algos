
my_list =[1, 1, 1, 5, 5, 3, -1, 15, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2, 0, 11, 6, 's', 'q'] 

def CountFrequency(my_list): 
  
    # Creating an empty dictionary and stack 
    freq = {}
    my_stack = [] 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
  
    for key, value in freq.items(): 
        #print ("% d : % d"%(key, value))
        print(key,':',value)
        if value == 1:
            my_stack.append(key)
            print('my_stack = ',my_stack) 
  
    # this part will sort values based on the frequency

    print(sorted(freq.items(), key = lambda kv:([0], kv[1]))) 
    # swapping 0, 1 will sort either key or value

CountFrequency(my_list) 