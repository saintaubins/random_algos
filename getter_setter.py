class Bar(object):
    def __init__(self):
        self.value = ''
    def __get__(self, instance, owner):
        print("get from Bar class")
        return self.value
    def __set__(self, instance, value):
        print("set from Bar class")
        self.value = value
    def __delete__(self, instance):
        print("deleted in from Bar class")
        del self.value

class Foo(object):
    bar = Bar()

#f = Foo()
#f.bar = 10
#print(f.bar)
#del f.bar
x = 5
y = 7

# def swap(x,y):
#     x,y = y,x
#     print('x= ',x,'y=', y)

# swap(x,y)

my_str = 'a' 
print(my_str)
my_str = 1
print(my_str) 
