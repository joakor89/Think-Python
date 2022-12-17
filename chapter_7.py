# Chapter 7 Iteration > Think python
import math


'''
It's the ability to run a block of 
statements repeatedly.
'''

# Reassigning


'''
x = 5 
print(x)
y = 7 
print(y)

a = 5
b = a
a = 3
print(b)
print( a == b)
'''


# Updating variables

# This is known as increment & substracting
# is known as decrement


'''
x = x + 1
print(x)

'''

# The while statement
'''
in computer program, repetition is also called iteration
'''

# This kind of flow is call loop
# Always be careful with infinite loops

'''
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')

countdown(10)
'''

#

'''
def sequence(n):
    while n != 1:
        print(int(n))
        if n % 2 == 0:
            n = n / 2
        else:
            n = n*3 + 1

sequence(20)
'''

# Break 

'''
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)

print('Done!')
'''

# Square root

a = 4 
x = 3
y = (x + a/x) / 2

print(y)

x = y
y = (x + a/x) / 2
print(y)

while True:
    print(x)
    y = (x + a/x) / 2
    if y == x:
        break
    x = y


'''
epsilon = 4
if abs(y-x) < epsilon:
    break
'''

# Exercises 

# Exercise 7-1
def mysqrt(a):
	epsilon = 0.00001
	x = 5.00000
	while True:
		y = (x + a/x) / 2
		if abs(y - x) < epsilon:
			return y
			break
		x = y
		
import math
print (mysqrt( 4 ))

def test_square_root():
	print ("a	mysqrt(a)	math.sqrt(a)	diff")
	print ("-	---------	------------	----")
	for a in range(1, 10):
		print ("%.1f	%.5f	        %.5f	        %f" % (a,mysqrt(a), math.sqrt(a), mysqrt(a)-math.sqrt(a)))
		
test_square_root()

# Exercise 7-2


# Exercise 7-3
def factorial(n):
    """Computes factorial of n recursively."""
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


def estimate_pi():
    """Computes an estimate of pi.
    Algorithm due to Srinivasa Ramanujan, from 
    http://en.wikipedia.org/wiki/Pi
    """
    total = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        num = factorial(4*k) * (1103 + 26390*k)
        den = factorial(k)**4 * 396**(4*k)
        
        total += num / den
        term = factor * num/den
        
        if abs(term) < 1e-15:
            break
        k += 1
    
    return 1 / (factor * total)

print(estimate_pi())







































