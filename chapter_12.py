# Chapter 12 Tuples > Think python
import math 

# Tuples are Immutable

'''
a tuple is a sequence of values, these can be 
any type and are indexed by integers.
Pretty similar to list 
Tuples are immutable
'''

tt = 'a', 'b', 'c', 'd', 'e'
print(tt)
tt1 = ('a', 'b', 'c', 'd', 'e')
print(tt1)
t1 = 'a'
print(type(t1))
t2 = ('a')
print(type(t2))
t = tuple()
print(t)
t = tuple('lupins')
print(t)
t = ('a', 'b', 'c', 'd', 'e')
print(t[0])
print(t[1:3])
t = ('A',) + t[1:]
print(t)
print((0,1,2) < (0,3,4))
print((0, 1, 2000000) < (0, 3, 4))

# Tuple assigment

'''
temp = a 
a = b 
b = temp
'''

# Or it just can be elegantly tuple assignment
'''
a, b = b, a
a, b = 1, 2, 3
'''

# Tuples as return values
'''
divmod is a built-in function that takes two 
arguments and returns a tuple of two values
'''
t = divmod(7, 3)
print(t)
quot, rem = divmod(7, 3)
print(quot)
print(rem)

def min_max():
    return min(t), max(t)

# Variable-length argument tuples

def printall(*args):
    print(args)

printall(1, 2.0, '3')

t = (7, 3)
print(divmod(*t))

# List & tuples 

s = 'abc'
print(s)
t= [0, 1, 2]
print(t)
zip(s,t)
print(zip)

for pair in zip(s, t):
    print(pair)

# Zip object
print(list(zip(s, t)))
print(list(zip('Anne', 'Elk')))


t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print(number, letter)


def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

for index, element in enumerate('abc'):
    print(index, element)


# Dictionaries & Tuples
d = {'a':0, 'b':1, 'c':2}
t = d.items()
print(t)

for key, value in d.items():
    print(key, value)

t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)

d = dict(zip('abc', range(3)))
print(d)

# Exercise 
# 12-1
'''
def most_frequent(s):
    """Sorts the letters in s in reverse order of frequency.
    s: string
    Returns: list of letters
    """
    hist = make_histogram(s)

    t = []
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)

    res = []
    for freq, x in t:
        res.append(x)

    return res
    

def make_histogram(s):
    """Make a map from letters to number of times they appear in s.
    s: string
    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist


def read_file(filename):
    """Returns the contents of a file as a string."""
    return open(filename).read()


if __name__ == '__main__':
    string = read_file('emma.txt')
    letter_seq = most_frequent(string)
    for x in letter_seq:
        print(x)
'''

# 12-2

'''
def signature(s):
    """Returns the signature of this string.
    Signature is a string that contains all of the letters in order.
    s: string
    """
    # TODO: rewrite using sorted()
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def all_anagrams(filename):
    """Finds all anagrams in a list of words.
    filename: string filename of the word list
    Returns: a map from each word to a list of its anagrams.
    """
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)

        # TODO: rewrite using defaultdict
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def print_anagram_sets(d):
    """Prints the anagram sets in d.
    d: map from words to list of their anagrams
    """
    for v in d.values():
        if len(v) > 1:
            print(len(v), v)


def print_anagram_sets_in_order(d):
    """Prints the anagram sets in d in decreasing order of size.
    d: map from words to list of their anagrams
    """
    # make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort()

    # print the sorted list
    for x in t:
        print(x)


def filter_length(d, n):
    """Select only the words in d that have n letters.
    d: map from word to list of anagrams
    n: integer number of letters
    returns: new map from word to list of anagrams
    """
    res = {}
    for word, anagrams in d.items():
        if len(word) == n:
            res[word] = anagrams
    return res


if __name__ == '__main__':
    anagram_map = all_anagrams('words.txt')
    print_anagram_sets_in_order(anagram_map)

    eight_letters = filter_length(anagram_map, 8)
    print_anagram_sets_in_order(eight_letters)
'''


# 12-3
'''
def metathesis_pairs(d):
    """Print all pairs of words that differ by swapping two letters.
    d: map from word to list of anagrams
    """
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    print(word1, word2)


def word_distance(word1, word2):
    """Computes the number of differences between two words.
    word1, word2: strings
    Returns: integer
    """
    assert len(word1) == len(word2)

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1

    return count


if __name__ == '__main__':
    sets = anagram_sets.all_anagrams('words.txt')
    metathesis_pairs(sets)
'''

# 12-4

'''
def make_word_dict():
    """Reads a word list and returns a dictionary."""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d


"""memo is a dictionary that maps from each word that is known
to be reducible to a list of its reducible children.  It starts
with the empty string."""

memo = {}
memo[''] = ['']


def is_reducible(word, word_dict):
    """If word is reducible, returns a list of its reducible children.
    Also adds an entry to the memo dictionary.
    A string is reducible if it has at least one child that is 
    reducible.  The empty string is also reducible.
    word: string
    word_dict: dictionary with words as keys
    """
     # if have already checked this word, return the answer
    if word in memo:
        return memo[word]

    # check each of the children and make a list of the reducible ones
    res = []
    for child in children(word, word_dict):
        if is_reducible(child, word_dict):
            res.append(child)

    # memoize and return the result
    memo[word] = res
    return res


def children(word, word_dict):
    """Returns a list of all words that can be formed by removing one letter.
    word: string
    Returns: list of strings
    """
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)
    return res


def all_reducible(word_dict):
    """Checks all words in the word_dict; returns a list reducible ones.
    word_dict: dictionary with words as keys
    """
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res


def print_trail(word):
    """Prints the sequence of words that reduces this word to the empty string.
    If there is more than one choice, it chooses the first.
    word: string
    """
    if len(word) == 0:
        return
    print(word, end=' ')
    t = is_reducible(word, word_dict)
    print_trail(t[0])


def print_longest_words(word_dict):
    """Finds the longest reducible words and prints them.
    word_dict: dictionary of valid words
    """
    words = all_reducible(word_dict)

    # use DSU to sort by word length
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    # print the longest 5 words
    for _, word in t[0:5]:
        print_trail(word)
        print('\n')


if __name__ == '__main__':
    word_dict = make_word_dict()
    print_longest_words(word_dict)

'''



























