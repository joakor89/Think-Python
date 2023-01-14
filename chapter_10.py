# Chapter 10 List > Think python
import math
import bisect
import time

'''
a lsit is a sequence of values and these cane be
any type of. The values in a lsit are called elements
or sometime just items
this can be assigned to variables
'''
#
'''
random = ['spam', 2.0, 5, [10, 20]]
print(random)

cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [42, 123]
empty = []
print(cheeses, numbers, empty)
'''


# List are mutables 

'''
print(cheeses[0])
numbers = [42, 123]
numbers[1] = 5
print(numbers)
'''


# the in operator also works on list
'''
cheeses = ['Cheddar', 'Edam', 'Gouda']
print('Edam' in cheeses)
print('Brie' in cheeses)
'''

# Traversing a list
'''
the most common way to traverse 
a list is with a for loop
'''

'''
for cheese in cheeses:
    print(cheese)


for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    print(numbers)

for x in []:
    print('This never happens')
'''

# List operations
'''
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

print([0] * 4)
print([1, 2, 3] * 3)
'''

# list slices 
'''
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)
'''

# List methods
'''
t = ['a', 'b', 'c']
t.append('d')
print(t)

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)
'''

# Map, filter and reduce

def add_all(t):
    total = 0
    for x in t:
        total += x
    return total


t = [1, 2, 3]
print(sum(t))

t = ['a', 'b', 'c']

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalzie())
    return res

# Deliting elements 

t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)

t = ['a', 'b', 'c']
del t[1]
print(t)

# similarly
t = ['a', 'b', 'c']
t.remove('b')
print(t)

t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)

# List & strings
s = 'spam'
t = list(s)
print(t)

s = 'pining for the fjords'
t = s.split()
print(t)

s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
print(t)

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
s = delimiter.join(t)
print(s)


# Objects & values
a = 'banana'
b = 'banana'
print(a is b)

'''
In this second example they are equivalent
but not identical
'''
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

# Aliasing 
'''
refers to an object and you assign b = a
then both variables refer to the same object
'''

a = [1, 2, 3]
b = a 
print(b is a)

# List of arguments
def delete_head(t):
    del t[0]

letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)

t1 = [1, 2]
t2 = t1.append(3)
print(t1)
print(t2)

t3 = t1 + [4]
print(t1)
print(t3)

# Exercise 10-1

def nested_sum(t):
    """Computes the total of all numbers in a list of lists.
   
    t: list of list of numbers
    returns: number
    """
    total = 0
    for nested in t:
        total += sum(nested)
    return total

# Exercise 10-2
def cumsum(t):
    """Computes the cumulative sum of the numbers in t.
    t: list of numbers
    returns: list of numbers
    """
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res


# Exercise 10-3
def middle(t):
    """Returns all but the first and last elements of t.
    t: list
    returns: new list
    """
    return t[1:-1]

# Exercise 10-4
def chop(t):
    """Removes the first and last elements of t.
    t: list
    returns: None
    """
    del t[0]
    del t[-1]


# Exercise 10-5
def is_sorted(t):
    """Checks whether a list is sorted.
    t: list
    returns: boolean
    """
    return t == sorted(t)

# Exercise 10-6
def is_anagram(word1, word2):
    """Checks whether two words are anagrams
    word1: string or list
    word2: string or list
    returns: boolean
    """
    return sorted(word1) == sorted(word2)


# Exercise 10-7
def has_duplicates(s):
    """Returns True if any element appears more than once in a sequence.
    s: string or list
    returns: bool
    """
    # make a copy of t to avoid modifying the parameter
    t = list(s)
    t.sort()

    # check for adjacent elements that are equal
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False


# Exercise 10-8

def main():
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))

    t = [1, 2, 3]
    print(cumsum(t))

    t = [1, 2, 3, 4]
    print(middle(t))
    chop(t)
    print(t)

    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))

    print(is_anagram('stop', 'pots'))
    print(is_anagram('different', 'letters'))
    print(is_anagram([1, 2, 2], [2, 1, 2]))

    print(has_duplicates('cba'))
    print(has_duplicates('abba'))

# Exercise 10-9

def make_word_list1():
    """Reads lines from a file and builds a list using append."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def make_word_list2():
    """Reads lines from a file and builds a list using list +."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t


start_time = time.time()
t = make_word_list1()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

start_time = time.time()
t = make_word_list2()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')


# Exercise 10-10

def make_word_list():
    """Reads lines from a file and builds a list using append.
    returns: list of strings
    """
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    returns: True if the word is in the list; False otherwise
    """
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i+1:], word)


def in_bisect_cheat(word_list, word):
    """Checks whether a word is in a list using bisection search.
    Precondition: the words in the list are sorted
    word_list: list of strings
    word: string
    """
    i = bisect.bisect_left(word_list, word)
    if i == len(word_list):
        return False

    return word_list[i] == word


if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect(word_list, word))

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect_cheat(word_list, word))


# Exercise 10-11

def reverse_pair(word_list, word):
    """Checks whether a reversed word appears in word_list.
    word_list: list of strings
    word: string
    """
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)
        

if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in word_list:
        if reverse_pair(word_list, word):
            print(word, word[::-1])

# Exercise 10-12
def interlock(word_list, word):
    """Checks whether a word contains two interleaved words.
    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds) 
        

def interlock_general(word_list, word, n=3):
    """Checks whether a word contains n interleaved words.
    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True
        

if __name__ == '__main__':
    word_list = make_word_list()
    
    for word in word_list:
        if interlock(word_list, word):
            print(word, word[::2], word[1::2])

    for word in word_list:
        if interlock_general(word_list, word, 3):
            print(word, word[0::3], word[1::3], word[2::3])

if __name__ == '__main__':
    main()





















