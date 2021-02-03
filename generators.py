# working with generators

def topten():
    n = 1
    while n <= 10:
        i = n * n
        yield i
        n += 1 

values = topten()

for i in values:
    print(i)