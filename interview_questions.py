import math
#import pdb; pdb.set_trace()
#breakpoint()
#python -m pdb interview_questions.py
#import inspect

class Prime_num:
    def __init__(self, num):
        self.num = num

    def find_prime(self):

        abs_val = abs(num)
        root_val = math.sqrt(abs_val)
        root_val = int(root_val)
        print('root_val:',root_val)
        if abs_val <= 1:
            print('number is zero or 1 and cannot be prime')
            print('$' * abs_val)
           
        elif abs_val == 2 or abs_val == 3:
            print('number is', abs_val ,  'and is prime')
            print('$' * abs_val)
           
        elif abs_val % 2 == 0:
            print('number is not prime, because it is an even number')
            print('$' * abs_val)
        elif num >= 3:
            i = 3
            #breakpoint()
            while i <= 1+root_val:
                if num % i == 0:
                    print(num,'is not prime')
                    break
                else:
                    print(num,'is prime')
                    break
                i += 2

num = 2
p = Prime_num(num)
x = list(range(0, 20))
x_e = [i for i in x if i%2 == 0]
x_o = [i for i in x if i%2 != 0]
print('x_e = ',x_e)
print('x_o = ',x_o)
print(p.find_prime())
#print(inspect.getsource(count))


##################### 2-1-21 Apple interview question 6;45pm EST ########################
a = [22,25]
b = ['python', 'programming']

"""return odd-indexed list from list a -> [25,46]""" 

for i,v in enumerate(a):
    if i % 2 != 0:
        print(v, a[i])
    

# slicing ->
print(a[1:len(a):2])
print(a[1::2])
# then second question merge a:b into key value
res = {}
for k,v in zip(a,b):
    res[k] = v
print(res)

print({k:v for k,v in zip(a,b)})

## my solution
print(dict(zip(a,b)))

