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


#####################################3
#spaces between operators



i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)


def complex(real, imag=0.0):
    return magic(r=real, i=imag)

########################
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()


FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )

# FILES = ['setup.cfg', 'tox.ini',]         # this code not clean the above is the clean version of it
# initialize(FILES, error=True,)
##########################################

try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)

################################################
import math

def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)