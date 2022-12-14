# Chapter 5 Conditionals & recursion > Think python
import turtle


# Floor division & modulus

minutes = 105
min = minutes / 60
print(min)

# Floor division returns the integer number
hours = minutes // 60
print(hours)

# Modulus operator % divides two numbers and returns the remainder

remainder = minutes % 60
print(remainder)

# Boolean expresions

boo = 5 == 5
print(boo)
bool = 5 == 6
print(bool)

boole = print(type(True))
boolea = print(type(False))

# Logical operators

'''
x > 0 or x < 10
n%2 == 0 or n%3 == 0 
'''

# Conditional execution

x = 4
if x > 0:
    print('x is a positive')

if x < 0:
    pass

# Alternative execution

y = 6
if y % 2 == 0:
    print('y is even')
else:
    print('y is odd')


# Chained conditionals

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

'''
a = 3
b = 6
c = 9

if choice == 'a':
    draw_a()
if choice == 'b':
    draw_b()
elif choice == 'c':
    draw_c()
'''

# Nested conditional 

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')

if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')

if 0 < x and x < 10:
    print('x is a positive single-digit number.')

if 0 < x < 10:
    print('x is a positive single-digit number.')

# Recursion 
# a function that calls itself is recursive; the process
# of executing it is called recursion
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(-1)

countdown(10)

# Let's try another example
'''
def print_n(s, n):
    if n <= 0:
        n = 4
        s = 5
        return
    print(s)
    print_n(s, n-1)
'''
# Infinite recursion
'''
def recurse():
    recurse()
'''

# Keyboard input

text = input('What are you waiting for?')
print(text)

# Exercises

# 5-3
# Triangle A
def is_triangle(a, b, c):
       if a <= b+c:
            if b <= a+c:
                 if c <= a+b:
                    return 'yes'
                 else:
                    return 'no'
            else:
                 return 'no'
       else:
            return 'no'

is_triangle(1, 12, 1)
'no'

# Triangle B
def is_triangle(a, b, c):
       if a<=b+c and b<=a+c and c<=a+b:
           return 'yes'
       else:
           return 'no'

is_triangle(1, 12, 3)
'no'

# 5-4
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)
# 5-5
def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


# 5-6

def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)


bob = turtle.Turtle()

bob.pu()
bob.goto(-150, 90)
bob.pd()
snowflake(bob, 300)

turtle.mainloop()

















