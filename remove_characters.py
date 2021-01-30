import re

original_string = '!(Hell@o)#'
characters_to_remove = '!()@#'

new_string = original_string
for character in characters_to_remove:
    new_string = new_string.replace(character,'')

print(new_string)

org_string = 'Hello there!@#$%^&*'
stuff_to_remove = '!@#$%^&*('

my_string = org_string
pattern = '[' + stuff_to_remove + ']'
my_string = re.sub(pattern,'',org_string)

print(my_string)

random_string = 'this i#$%^&*s a random string!@#$%^@#$%'
new_random_string = ''.join(e for e in random_string if e.isalnum())

print(new_random_string)
