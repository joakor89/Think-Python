# Chapter 8 Strings > Think python

'''
A string is a sequence of characters and an ordered collection
of other values.
'''

# A string of sequence

fruit = 'banana'
# the expression in square brackets is called an 'Index'
letter = fruit[1]
print(letter)
i = 2
print(fruit[i])

# len
'''
len is a built-in function that returns the number of characters
in a string:
'''
print(len(fruit))
length = len(fruit)
print(length)
last = fruit[length - 1]
print(last)

# Traversal with a for Loop

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

print(('***' * 5))

for letter in fruit:
    print(letter)

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print(letter + suffix)

# String slices

'''
a segment of a string is called a slice
'''

s = 'Monty Python'
print(s[0:5])
print(s[6:12])

print(('***' * 5))

print(fruit[:3])
print(fruit[3:])

# print(fruit[3:3])

# Strings are Immutable
greetings = 'Hello, world!'
# print(greetings[0] = 'J')
print(greetings)
print(('***' * 5))

new_greetings = 'J' + greetings[1:]
print(new_greetings)

# Searching
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(fruit)

# Looping and counting
'''
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1

print(a)
'''

# Strings methods
'''
word = 'banana'
new_word = word.append(a)
print(new_word)
'''

word = 'banana'
new_word = word.find('a')
new_word = word.find('na')
print(new_word)

print(('***' * 5))
name = 'bob'
name.find('b', 1, 2)
print(name)

# The in operator
rack = 'a' in 'banana'
print(rack)

seed = 'seed' in 'banana'
print(seed)

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('apples', 'oranges')

print(('***' * 5))
if word == 'banana':
    print('All right, bananas')

print(('***' * 5))

if word < 'banana':
    print('Your word, ' + word + ', comes after banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bananas.')

print(('***' * 5))

# Exercise 

# Exercise 8-4
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        return flag


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


# Exercise 8-5
def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.
    letter: single-letter string
    n: int
    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.
    word: string
    n: integer
    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res


if __name__ == '__main__':
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))










