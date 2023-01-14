# Chapter 3  Functions > Think python
import math

'''
The coding program on this script is slighly diferent from since
is performed on Visual studio code.
'''

# Functions calls
print(type(42))
print(int(32))
'''
print(int('Hello'))
'''
print(int(3.99999))
print(int(-2.3))

# Float converts integer and strings to floating-point numbers
print(float(32))
print(float('3.14159'))
# Strings: (str) convert its argument to a string
print(str(32))
print(str(3.14159))

# Math functions
'''
math module provides most of familiar mathematical functions
'''
print(math)
'''
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print(decibels)
'''

radians = 0.7
heigth = math.sin(radians)
print(heigth)

degrees = 45
radians = degrees / 100.0 * math.pi
print(radians)
result =  math.sin(radians)
print(result)

square_root = math.sqrt(2) / 2.0
print(square_root)

# Composition 
degrees = 45
x = math.sin(degrees/360.0 * 2 * math.pi)
print(x)

z = math.exp(math.log(x + 1))
print(z)

'''
minutes = hours * 60
hours * 60 = minutes
'''

# Adding new functions
'''
a function definition specifies the name of a new function and 
the sequence of statements that run when the function is called
def is a keyword that indicates that this is a function
1) the first line is the "header"
2) the rest is called "body"
'''

#Definitions and uses

def print_lyrics():
    print("I'm a lumberjack, and I'm okay. ")
    print("I sleep all night and I work all day. ")


print(type(print_lyrics))
print(print_lyrics)

def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()

# Parameters and arguments

'''
inside the function, the arguments are assigned to variables called 
"parameters" 
'''

def print_twice(bruce):
    print(bruce)
    print(bruce)


print_twice('Spam')
print_twice(42)
print_twice(math.pi)
print_twice('Spam' * 4)

# Yo can also use a variable as an argument:
michael = 'Eric, the half a bee.'
print_twice(michael)

# Variables and parameters are local

'''
when you create a variable inside a function, it is loca, which
means that it only exist inside the function
'''
def cat_twice(part_1, part_2):
    cat = part_1 + part_2
    print_twice(cat)



line1 = 'Bing tiddle '
line2 = 'tiddle bang.'
cat_twice(line1, line2)

# Stack diagrams

'''
a "frame" is a box with the name of a function beside it and 
the parameters and variables of the function inside it

"stake diagram" show the value of each variable, but also
show the function each variable belongs to.

"tracebak" it tells you what program file the error occurred
in and what line and function were executing at the time.
'''
# Fruitful functions & void functions

a = math.cos(radians)
print(a)

golden = math.cos(math.sqrt(5) + 1) / 2
print(golden)

s_r_f = math.sqrt(5)
print(s_r_f)

outcome = print_twice('Bing !')
# None
print(outcome)
# what is None?
print(type(None))

# Exercises
# Exercise 3-1

def right_justify(s):
    print (' '*(70-len(s))+s)

right_justify('monty')


'''
def right_justify(s):
    total_length = 70
    current_length = len(s)
    current_string = s
    while current_length < total_length:
        current_string = " " + current_string
        current_length = len(current_string)
    print(current_string)


right_justify('monty')

'''















































































