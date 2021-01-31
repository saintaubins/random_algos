from collections import defaultdict

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(names), len(colors))

for i in range(n):
    print(names[i], '-->', colors[i])


for name, color in zip(names, colors):
    print(name, '-->', color)

for color in sorted(colors):
    print(color)

for color in sorted(colors, reverse=True):
    print(color)

'''
def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0

print(sorted(colors, cmp=compare_length))

slow complexity nlogn

'''
print(sorted(colors, key=len))

'''

not recommended
blocks = []
while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)

recommended
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)

'''

def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1

    return i 

seq = ['','stuff','more stuff','tgt', 11]

print(find(seq, 'hello'))


# looping over dictionary keys

d = {'matthew':'blue', 'rachel':'green', 'raymond':'red'}

for k in d:
    print(k)

'''
for k in d.keys():
    if k.startswith('r'):
        d.pop(k)
print(d)
'''

for k in d:
    print(k, '-->', d[k])

for k, v in d.items():
    print(k,'-->', v)

d_colors = ['red', 'green', 'red', 'blue', 'green', 'red']
d_d = {}
'''
for color in d_colors:
    if color not in d_d:
        d_d[color] = 0
    d_d[color] += 1

'''
for color in d_colors:
    d_d[color] = d_d.get(color, 0) + 1

print(d_d)

# grouping with dictionaries

names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'mellissa',
'judith', 'charlie']

d_d_d = {}
'''
standard way
for name in names:
    key = len(name)
    if key not in d_d_d:
        d_d_d[key] = []
    d_d_d[key].append(name)
'''
# faster way
d_d_d_d = defaultdict(list)
for name in names:
    key = len(name)
    d_d_d_d[key].append(name)

print(d_d_d_d)

# unpacking sequences

p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'

fname, lname, age, email = p

print(type(p), p)

'''
#not recommended
def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print(x)
        t = y
        y = x + y
        x = t
'''
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print(x)
        x, y = y, x+y

print(fibonacci(12))

# Simultaneous state updates

'''
brute froce slow way

tmp_x = x + dx * t
tmp_y = y + dy * t
tmp_dx = influence(m, x, y, dx, dy, partial='x')
tmp_dy = influence(m, x, y, dx, dy, partial='y')
x = tmp_x
y = tmp_y
dx = tmp_dx
dy = tmp_dy


propper, faster way
x, y, dx, dy = (x + dx + t,
                y + dy + t,
                influence(m, x, y, dx, dy, partial='x'),
                influence(m, x, y, dx, dy, partial='y') )

'''


# Concatenating strings

s_names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'mellissa',
'judith', 'charlie', 'sem']

'''
not recommended
s = names[0]
for name in names[1:]:
    s += ', ' + name
print(s)

'''

# recommended way

print(', '.join(s_names))

q_names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'mellissa',
'judith', 'charlie', 'sem']

'''
not recommended
del q_names[0]
q_names.pop(0)
q_names.insert(0, 'mark')

'''
# recommended way

from collections import deque

q_names = deque(['raymond', 'rachel', 'matthew', 'roger', 'betty', 'mellissa',
'judith', 'charlie', 'sem'])

del q_names[0]
q_names.popleft()
q_names.appendleft('mark')
print(q_names)

'''
not recommended
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page

'''

# recommended way
import requests
from functools import wraps
import urllib.request

# caching decorator should be in a utlis file

def cache(func):
    saved = {}
    @wraps(func)
    def newfunc(*args):
        if args in saved:
            return newfunc(*args)
        result = func(*args)
        saved[args] = result
        return result
    return newfunc

url = 'http://www.google.com'
@cache
def web_lookup(url):
    return urllib.request.urlopen(url).read()

#print(web_lookup(url))

# How to open and close files

'''
not recommended

f = open('data.txt')
try:
    data = f.read()
finally:
    f.close()

'''

# recommended way

with open('rev_words.py') as f:
    data = f.read()
print(data)

# how to use locks

'''
not recommended

# make a lock
lock = threading.Lock()

# Old-way to use a lock
lock.acquire()
try:
    print('Critical section 1')
    print('Critical section 2')
finally:
    lock.release()

'''

# new way to use a lock

# make a lock
import threading
lock = threading.Lock()

with lock:
    print('Critical section 1')
    print('Critical section 2')

# Factor out tempory contexs

from contextlib import redirect_stdout
with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)

# list comprehension and generator expressions

'''
not recommended

result = []
for i in range(10):
    s = i ** 2
    result.append(s)
print(sum(result))

'''
# recommended way

print(sum([i**2 for i in range(10)]))

print(sum(i**2 for i in range(10)))




