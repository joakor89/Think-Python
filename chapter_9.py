# Chapter 9 Case study: Word play > Think python

import csv 
import textwrap

fin = open('words.txt')
fin.readline()
'a\ar\n'

line = fin.readline()
word = line.strip()
print(word)

'''

fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)
'''

# Inner exercises
# 9-1
'''
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print (word)
'''

# 9-2

'''
fin = open('words.txt')

def has_no_e(word):
    for char in word:
        if char in 'Ee':
            return False
    return True  

count = 0
for line in fin:
    word = line.strip()
    if has_no_e(word):
        count += 1
        print (word)

percent = (count / 113809.0) * 100

print (str(percent)) + "% of the words don't have an 'e'."
'''


# 9-3

'''
fin = open('words.txt')

def avoids(word,letter):
    for char in word:
        if char in letter:
            return False
    return True


letter = raw_input('What letters to exclude? ')
count = 0
for line in fin:
    word = line.strip()
    if avoids(word, letter):
        count += 1
        print word

percent = (count / 113809.0) * 100

print (str(percent) + "% of the words don't have " + letter + '.')
'''

# 9-4
'''
def uses_only(word, letters):
    """returns true if word is made only out of letters  else flase"""
    for letter in word:
        if letter not in letters:
            return False
    return True
'''

# Search 
'''
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True

def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True

def uses_all(word, required):
    for letter in required:
        if letter not in word:
            return False
    return True
'''

# Program development plan called reduction to a previously
# solved problem
'''
def uses_all(word, required):
    return uses_only(required, word)
'''


# Looping with Indeces
'''
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

'''

# An alternative recursion would be:
'''
def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])
'''

# Using a while loop
'''
def is_abecedarian(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i+1
    return True

print(is_abecedarian(word))
'''

# Palindrome
'''
def is_palindrome(word):
    i = 0
    j = len(word)-1

    while i<j:
        if word[i] != word[j]:
            return False
        i = i+1
        j = j-1

    return True

# Or reduced by

def is_palindrome(word):
    return is_reverse(word, word)
'''

# Exercise 9-7
def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.
    
    word: string
    returns: bool
    """
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            i = i + 1 - 2*count
            count = 0
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')

# Exercise 9-8
def has_palindrome(i, start, length):
    """Checks if the string representation of i has a palindrome.
    i: integer
    start: where in the string to start
    length: length of the palindrome to check for
    """
    s = str(i)[start:start+length]
    return s[::-1] == s

    
def check(i):
    """Checks if the integer (i) has the desired properties.
    i: int
    """
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))


def check_all():
    """Enumerate the six-digit numbers and print any winners.
    """
    i = 100000
    while i <= 999996:
        if check(i):
            print(i)
        i = i + 1


print('The following are the possible odometer readings:')
check_all()
print()

# Exercise 9-9

def str_fill(i, n):
    """Returns i as a string with at least n digits.
    i: int
    n: int length
    returns: string
    """
    return str(i).zfill(n)


def are_reversed(i, j):
    """Checks if i and j are the reverse of each other.
    i: int
    j: int
    returns:bool
    """
    return str_fill(i, 2) == str_fill(j, 2)[::-1]


def num_instances(diff, flag=False):
    """Counts the number of palindromic ages.
    Returns the number of times the mother and daughter have
    palindromic ages in their lives, given the difference in age.
    diff: int difference in ages
    flag: bool, if True, prints the details
    """
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff

        # assuming that mother and daughter don't have the same birthday,
        # they have two chances per year to have palindromic ages.
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
            count = count + 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count
    

def check_diffs():
    """Finds age differences that satisfy the problem.
    Enumerates the possible differences in age between mother
    and daughter, and for each difference, counts the number of times
    over their lives they will have ages that are the reverse of
    each other.
    """
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1

print('diff  #instances')
check_diffs()

print()
print('daughter  mother')
num_instances(18, True)



















