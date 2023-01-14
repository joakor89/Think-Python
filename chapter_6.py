import math

# Return values

radius = 6
area = 12
radians = 4
'''
e = math.exp(1.0)
height = radius * math.sin(radians)
print(height)

# Fruitful example
def area(radius):
    a = math.pi * radius**2
    return a 
'''

'''
Python has a built-in function to calculate
absolute value

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x 
'''

'''
def absolute_value(x):
    if x < 0:
        return -x
    if x > 0:
        return x 

absolute_value(0)
'''

# Incremental development
# the goal of Incremental development is to avoid long
# debugging sessions
'''
def distance(x1, y1, x2, y2):
    return 0.0

distance(1, 2, 3, 4)

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print('dx is', dx)
    print('dy is', dy)
    return 0.0

distance(1, 4, 6, 8)
'''
#

'''
def distances(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    rest = math.sqrt(dsquared)
    # should use scaffolding
    print(rest)
    return rest

distances(2, 4, 6, 8)

'''
# Composition

# Encapsulating a
'''
def circle_area(xc, yc, xp, yp):
    radius = distances(xc, yc, xp, yp)
    result = area(radius)
    print(result)
    return result
'''

# Encapsulating b
'''
def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))
'''

'''
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

print(is_divisible(6, 4))
print(is_divisible(6, 3))

def is_divisible(x, y):
    return x % y == 0

if is_divisible:
    print('x is divisible by y')

print(is_divisible(8, 4))
'''

# More recursion - factorial

'''
def factorial(n):
    if n == 0:
        return 1

print(factorial(0))

# Also
def factorials(n):
    if n == 0:
        return 1
    else:
        recurse = factorials(n - 1)
        outcome = n * recurse
        return outcome

print(factorials(3))
'''

# One more recursively example
# Fibonacci
'''
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(9))

'''

# Checking types

'''
factorial(1.5)
'''

'''
def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(9))
'''
# Debugging

'''
def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        print(space, 'returning', result)
        return result

print(factorial(4))
'''

# Exercise > chapter 6

# exercise 6-1
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square 

x = 1 
y = x + 1
print(c(x, y + 3, x + y))
# This return 9 90 & 8100

# Exercise 6-2
def ackermann(m, n):
    """Computes the Ackermann function A(m, n)
    See http://en.wikipedia.org/wiki/Ackermann_function
    n, m: non-negative integers
    """
    if m == 0:
        return n+1
    if n == 0:
        return ackermann(m-1, 1)
    return ackermann(m-1, ackermann(m, n-1))


print(ackermann(3, 4))

# Exercise 6-3
def first(word):
    """Returns the first character of a string."""
    return word[0]


def last(word):
    """Returns the last of a string."""
    return word[-1]


def middle(word):
    """Returns all but the first and last characters of a string."""
    return word[1:-1]


def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))


print(is_palindrome('allen'))
print(is_palindrome('bob'))
print(is_palindrome('otto'))
print(is_palindrome('redivider'))

