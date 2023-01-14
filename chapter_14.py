# Chapter 14 Files > Think python
import os
import dbm
import pickle
import wc
import shelve
import sys

# Persistance
'''
Some programs are persistent: they run for a long time
keep at least some of their data in permanent storage
and if you shut down or restart, then they pick up
where they left off
'''

# Reading and writing 

'''
To write a fil, you have to open it with mode 'w' as a
second parameter.
'''
fout = open('output.txt', 'w')
line1 = "This here's the wattle,\n"
print(fout.write(line1))
line2 = "the emblem of our land.\n"
print(fout.write(line2))
# fout.close()

# Format operator
x = 52
print(fout.write(str(x)))

camels = 42
print('%d' % camels)

print('I have spotted %d camels.' % camels)
print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))

'''
print('%d%d%d' % 1, 2)
print('%d % 'dollars')
'''

# Filenames & Paths

# CWD stands for "current working directory"
cwd = os.getcwd()
# Show the path

print(cwd)
print(os.path.abspath('output.txt'))
print(os.path.exists('output.txt'))

print(os.path.isdir('output.txt'))

'''
print(os.path.isdir('/Users/isisromero/Desktop/think_python'))
print(os.listdir(cwd))

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


def walk2(dirname):
    """Prints the names of all files in dirname and its subdirectories.
    This is the exercise solution, which uses os.walk.
    dirname: string name of directory
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))


if __name__ == '__main__':
    walk('.')
    walk2('.')

'''

# Catching exceptions
'''
try:
    fin = open('bad_file')
except:
    print('Something went wrong')
'''

# Databases
db = dbm.open('captions', 'c')
db ['cleese.png'] = 'Photo of John Cleese.'
print(db['cleese.png'])
db ['cleese.png'] = 'Photo of John Cleese doing a silly walk.'
print(db['cleese.png'])

'''
for key in db:
    print(key, db[key])
'''
db.close()

# Pickling

t = [1, 2, 3]
print(pickle.dumps(t))

t1 = [1, 2, 3]
s = pickle.dumps(t1)
t2 = pickle.loads(s)
print(t2)

print(t1 == t2)
print(t1 is t2)

# Pipes
'''
cmd = 'ls -l'
fp = os.popen(cmd)
res = fp.read()
print(res)
stat = fp.close()
print(stat)

filename = 'book.text'
cmd = 'md5sum ' + filename
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print(res)
print(stat)
'''

# Writing modules
'''
def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

print(linecount('wc.py'))
print(wc)
print(wc.linecount('wc.py'))

if __name__ == '__main__':
    print(linecount('wc.py'))

'''

# Exercise 

# 14-1
def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    fin = open(source, 'r')
    fout = open(dest, 'w')

    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)

    fin.close()
    fout.close()


def main():
    pattern = 'pattern'
    replace = 'replace'
    source = 'sed_tester.txt'
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)


if __name__ == '__main__':
    main()

# 14-2

'''
def store_anagrams(filename, anagram_map):
    """Stores the anagrams from a dictionary in a shelf.
    filename: string file name of shelf
    anagram_map: dictionary that maps strings to list of anagrams
    """
    shelf = shelve.open(filename, 'c')

    for word, word_list in anagram_map.items():
        shelf[word] = word_list

    shelf.close()


def read_anagrams(filename, word):
    """Looks up a word in a shelf and returns a list of its anagrams.
    filename: string file name of shelf
    word: word to look up
    """
    shelf = shelve.open(filename)
    sig = signature(word)
    try:
        return shelf[sig]
    except KeyError:
        return []


def main(script, command='make_db'):
    if command == 'make_db':
        anagram_map = all_anagrams('words.txt')
        store_anagrams('anagrams.db', anagram_map)
    else:
        print(read_anagrams('anagrams.db', command))


if __name__ == '__main__':
    main(*sys.argv)
'''


# 14-3
def walk(dirname):
    """Finds the names of all files in dirname and its subdirectories.
    dirname: string name of directory
    """
    names = []
    if '__pycache__' in dirname:
        return names

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names


def compute_checksum(filename):
    """Computes the MD5 checksum of the contents of a file.
    filename: string
    """
    # Note: installing md5sha1sum is required

    cmd = 'md5sum ' + filename
    return pipe(cmd)


def check_diff(name1, name2):
    """Computes the difference between the contents of two files.
    name1, name2: string filenames
    """
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)


def pipe(cmd):
    """Runs a command in a subprocess.
    cmd: string Unix command
    Returns (res, stat), the output of the subprocess and the exit status.
    """
    # Note: os.popen is deprecated
    # now, which means we are supposed to stop using it and start using
    # the subprocess module.  But for simple cases, I find
    # subprocess more complicated than necessary.  So I am going
    # to keep using os.popen until they take it away.

    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat


def compute_checksums(dirname, suffix):
    """Computes checksums for all files with the given suffix.
    dirname: string name of directory to search
    suffix: string suffix to match
    Returns: map from checksum to list of files with that checksum
    """
    names = walk(dirname)

    d = {}
    for name in names:
        if name.endswith(suffix):
            res, stat = compute_checksum(name)
            checksum, _ = res.split()

            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]

    return d


def check_pairs(names):
    """Checks whether any in a list of files differs from the others.
    names: list of string filenames
    """
    for name1 in names:
        for name2 in names:
            if name1 < name2:
                res, stat = check_diff(name1, name2)
                if res:
                    return False
    return True


def print_duplicates(d):
    """Checks for duplicate files.
    Reports any files with the same checksum and checks whether they
    are, in fact, identical.
    d: map from checksum to list of files with that checksum
    """
    for key, names in d.items():
        if len(names) > 1:
            print('The following files have the same checksum:')
            for name in names:
                print(name)

            if check_pairs(names):
                print('And they are identical.')


if __name__ == '__main__':
    d = compute_checksums(dirname='.', suffix='.py')
    print_duplicates(d)










