

def print_st_count(st):
    n = len(st)
    i = 0
    while i < n- 1:
        count = 1
        while (i < n - 1 and
               st[i] == st[i + 1]):
            count += 1
            i += 1
        i += 1
        print(st[i - 1] + str(count), end = '')
 
# Driver code 

st = "aabcccccaaa"
#print_st_count(st)

def check_for_prime(n):
    is_prime = False
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
            else:
                is_prime = True

    else:
        is_prime = False
    print(is_prime)

#check_for_prime(5)

def sort_stack ( stack ): 
    tmp_stack = create_stack() 
    while(is_empty(stack) == False): 
          
        tmp = top(stack) 
        pop(stack) 
  
        while(is_empty(tmp_stack) == False and
             int(top(tmp_stack)) > int(tmp)): 
            push(stack,top(tmp_stack)) 
            pop(tmp_stack) 
        push(tmp_stack,tmp) 
      
    return tmp_stack 
  
def create_stack(): 
    stack = [] 
    return stack 

def is_empty( stack ): 
    return len(stack) == 0

def push( stack, item ): 
    stack.append( item ) 
  
def top( stack ): 
    p = len(stack) 
    return stack[p-1] 

def pop( stack ): 
    if(is_empty( stack )): 
        print("Stack Underflow ") 
        exit(1) 
    return stack.pop() 
  
def prints(stack): 
    for i in range(len(stack)-1, -1, -1): 
        print(stack[i], end = ' ') 
    print() 
   
stack = create_stack() 
push( stack, str(34) ) 
push( stack, str(3) ) 
push( stack, str(31) ) 
push( stack, str(98) ) 
push( stack, str(92) ) 
push( stack, str(23) ) 
push( stack, str(100) )
  
print("Sorted numbers are: ") 
sortedst = sort_stack ( stack ) 
prints(sortedst)