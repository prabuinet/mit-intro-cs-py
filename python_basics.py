# -*- coding: utf-8 -*-


#Scalar objects in python:

5       #int
2.5     #float
True    #bool
None    #NoneType

type(5)
type(3.2)
type(False)
type(None)

#Type Cast
float(5)
int(2.5)


# operators on ints and floats
i = 5
j = 2
i + j   # sum
i - j   # difference
i * j   # product
i / j   # division
i // j  # => 2  integer division
i % j   # => 1  reminder
i ** j  # => 25 i to the power of j

# operator precedence
# 1. parantheses
# 2. **, *, /, + and -

# binding variabls and values

pi = 3.14159
pi_approx = 22/7

# abstracting expressions

radius = 2.2
area = pi * (radius ** 2)


#comparison operators on int and float
i >  j
i >= j
i <  j
i <= j
i == j
i != j

# a simple program
x = int(input('enter an integer:'))

if x % 2 == 0:
    print ('')
    print ('Even')
else:
    print('')
    print('Odd')

print('Done with conditional')







