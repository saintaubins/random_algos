my_string = '12345typy876'
new_string = ''
my_len = len(my_string)-1
count = 0
my_stack = []
while my_len != -1:
    new_string = my_string[my_len], my_string[count]
    my_stack.append(new_string)
    count += 1
    my_len -=1
#my_stack = list(my_stack)
for i in my_stack:
    print(i[0])
