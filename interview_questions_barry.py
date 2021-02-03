# def f(a, *b, **c):
#     print("{}{}".format(len(b), len(c)))
# f(10, 20, x=30)

# x =1 
# def f():
#     x = 2
#     return x

# class C(object):
#     x = 3
# if True:
#     x = 4
# f()
# C()
# print(x)

# t = (1,2)
# a,b = t 
# a,b = b,a 
# print("{}{}".format(a,b))

# str = '0123456789'
# print(str[-3:])

# print(max(x for x in range(12) if x %3 == 0))

# def LastNlines(fname, N): 
#     with open(fname) as file: 
#         for line in (file.readlines() [:N]): 
#             print(line, end ='') 
  
  
# N = 3
# try: 
#     LastNlines(fname, N) 
# except: 
#     print('File not found')

# fname = 'help.txt'
# file_ob = open(fname)
# n = 4
# for i, line in enumerate(file_ob):
#     if i+1 == n:
#         print(n, line)
#         break

# a_file = open("input.txt")

# number_of_lines = 10
#print(len(int(a_file))

# for i v in range(number_of_lines):
#     if i % 2 != 0:
#         line = a_file.readline()
#         print('i', i, 'line',line, 'v', v)

# with open('input.txt') as f:
#     lines = f.readlines()
#     count = 0
#     for line in lines:
#         if int(line) % 2 != 0 and count <= 5:
#             print(int(line))
#             count += 1

strParam = '<div><div><b></b></div></em>'.replace('>', '> ')
def HTMLElements(strParam):
    strParam = strParam.split()
    #print(strParam)
    freq = {}
    violated_params = []  
    open_tags = ['<b>', '<i>', '<em>', '<div>', '<p>']
    close_tags = ['</b>', '</i>', '</em>', '</div>', '</p>']

  
   
    for i in strParam:
        i_closed = i.replace('<','</')
        if i == '<div>' and '</div>' in strParam:
            strParam.pop(strParam.index('<div>'))
            strParam.pop(strParam.index('</div>'))
            #print(')
        if i == '<b>' and '</b>' in strParam:
            strParam.pop(strParam.index('<b>'))
            strParam.pop(strParam.index('</b>'))
            #print(strParam)
        if i == '<i>' and '</i>' in strParam:
            strParam.pop(strParam.index('<i>'))
            strParam.pop(strParam.index('</i>'))
            #print(strParam)
        if i == '<em>' and '</em>' in strParam:
            strParam.pop(strParam.index('<em>'))
            strParam.pop(strParam.index('</em>'))
            #print(strParam)
        if i == '<p>' and '</p>' in strParam:
            strParam.pop(strParam.index('<p>'))
            strParam.pop(strParam.index('</p>'))
            #print(strParam)
        print('i = ',i,'i_closed = ',i_closed, 'strParam = ',strParam)  
    for i in strParam:
        if i == '<div>' and strParam[1] != '</div>':
            print(strParam[1], 'needs to be </div>')
        if i == '<b>' and strParam[1] != '</b>':
            print(strParam[1], 'needs to be </b>')
        if i == '<i>' and strParam[1] != '</i>':
            print(strParam[1], 'needs to be </i>')
        if i == '<em>' and strParam[1] != '</em>':
            print(strParam[1], 'needs to be </em>')
        if i == '<p>' and strParam[1] != '</p>':
            print(strParam[1], 'needs to be </p>')
        
    #return strParam
HTMLElements(strParam)  
# keep this function call here 
#print(HTMLElements(input()))

    