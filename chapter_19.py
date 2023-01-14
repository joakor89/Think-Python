# Chapter 19 The Goodies > Think Python
import math
from collections import Counter 
from collections import defaultdict
from collections import namedtuple


# Conditional Expressions
x = 4
if x > 0:
    y = math.log(x)
else:
    y = float('nan')

# Or 

y = math.log(x) if x > 0 else float('nan')

# The factorial version

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def __init__(self, name, contents = None):
    self.name = name
    if contents == None:
        contents = []
    self.pouch_contents = contents

# Or 

def __init__(self, name, contents=None):
    self.name = name
    self.pouch_contents = [] if contents == None else contents

# List comprehensions 

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_all(t):
    return [s.capitalize() for s in t]

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res 

# Or 

def only_upper(t):
    return [s for s in t if s.isupper()]

# Generator Expressions

g = (x ** 2 for x in range(5))
print(g)

# Or 

print(next(g))
print(next(g))

for val in g:
    print(val)


print(sum(x ** 2 for x in range(5)))

# Any and all

print(any([False, False, True]))
print(any(letter == 't' for letter in 'monty'))

def avoids(word, forbidden):
    return not any(letter in forbidden for letter in word)

# Sets 

def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def subtract(d1, d2):
    return set(d1) - set(d2)

def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True
    return False

def has_duplicates(t):
    return len(set(t)) < len(t)

def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

# Or

def uses_only(word, available):
    return set(word) <= set(available)

# Counters

count = Counter('Parrot')
print(count)

print(count['d'])

def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)

count = Counter('parrot')
for val, freq in count.most_common(3):
    print(val, freq)

d = defaultdict(list)
t = d['new key']
print(t)
t.append('new value')
print(d)

def all_anagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d 

# First simplify version

def all_anagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        d[t].append(word)
        d.setdefault(t, [].append(word))
    return d

def all_anagrams(filename):
    d = defaultdict(list)
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        d[t].append(word)
    return d 

# Named tuples 

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g %g' % (self.x, self.y)

print(Point)

p = Point(1, 2)
print(p)
print(p.x, p.y)
# print(p[0], p[1])
# x, y = p 
# print(x, y)

# Gathering keywords args
def printall(*args):
    print(args)

printall(1, 2.0, '3')

def printall(*args, **kwargs):
    print(args, kwargs)

printall(1, 2.0, thrid = '3')
d = dict(x=1, y=2)
Point(**d)
Point(x=1, y=2)




























