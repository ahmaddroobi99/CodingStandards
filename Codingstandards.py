n1 = 10_000_000_000
n2 = 100_000_000
total = n1 + n2
print(total)
print(f'{total:,}')

names = ['corey', 'Chris', 'Dave', 'Travis']
# ____________________________________________
index = 0
for index, name in enumerate(names, start=1):
    print(index, name)
    index += 1

# __________________________________________
names = ['ahmad', 'mohammad ', 'rami', 'huda', 'waleed', 'mohannad ']
animals = ['cat', 'dog ', 'liaon', 'zebra', 'bird', 'rabite ']
universities = ['nnu', 'bzu ', 'Qou', 'Qu', 'ptuk', 'hi ']

for value in zip(names, animals, universities):
    print(value)

# ______________________________________________

a, b, *c, d = (1, 2, 3, 4, 8, 5)
print(a)
print(b)
print(c)
print(d)


class Person ():
    pass

person =Person()
# person.first ="Corey"
# person.last ="Schfer"

# first_key ='first'
# first_val ='Corey'
#
# setattr(person,first_key,first_val)
# first =getattr(person ,first_key)
#
# print(first)
#
#
# print(person.first)
# print(person.last)


person_info ={'first':'ahmad','last':'droobi'}

for key ,value in person_info.items():
    setattr(person ,key,value)
#
# print(person.first)
# print(person.last)

for key in person_info.keys():
    print(getattr(person,key))

#____________________________________________
from getpass import getpass

username =input('username: ')
password =getpass("passsword")   # onlt from cmd ok ?

print( 'Logging in ..')

