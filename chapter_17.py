# Chapter 17 Classes & Methods > Think Python

# Object-Oriented features 
'''
A method is a function that is associated
with a particular class (strings, lists
dictionaries and tuples.)
'''

# Printing objets
class Time:
    """Represents the time of day."""

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

start = Time()
start.hour = 9
start.minute = 45
start.second = 00
print(print_time(start))


class Time:
    def print_time(time):
        print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

Time.print_time(start)
# start.print_time()
'''
By convention, the first parameter of
a class is "self"
'''

class Time:
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

# Another example 
# Inside class Time:
'''
def increment(self, seconds):
    seconds += self.time_to_int()
    return int_to_time(seconds)
'''

# A more complicated example 
'''
def is_after(self, other):
    return self.time_to_int() > other.time_to_int()

end.is_after(start)

'''

# The Init Method

'''
"Initialization" is a special method that gets invoked
when an object is instantiated
'''

'''
def __init__(self, hour=0, minute=0, second=0):
    self.hour = hour
    self.minute = minute
    self.second = second

time = Time()
time.print_time()
time = Time(9)
time.print_time()
time = Time()
time.print_time(9, 45)
time.print_time()
'''


# The __str__ method
'''
__str__ is a special method that is supposed
to return a string representation of an object

def __str__(self):
    return '%.2d:%.2d:%2d' % (self.hour, self.minute, self.second)

time = time(9, 45)
print(time)

'''

# Operator overloading
'''
def __add__(self, other):
    seconds = self.time_to_init() + other.time_to_init()
    return int_to_time(seconds)

start = Time(9, 45)
duration = Time(1, 35)
print(start + duration)

'''

# Time-Base dispatch
'''
def __add__(self, other):
    if isinstance(other, Time):
        return self.add_time(other)
    else:
        return self.increment(other)

def add_time(self, other):
    seconds = self.time_to_int() + other.time_to_int()
    return int_to_time(seconds)

def increment(self, seconds):
    seconds += self.time_to_int()
    return int_to_time(seconds)


start = Time(9, 45)
duration = time(1, 35)
print(start + duration)
print(start + 1337)
# print(1337 + start)

def __radd__(self, other):
    return self.__add__(other)

print(1337 + start)
'''

# Polimorphism

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] +1
    return d 

t = ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam']
print(histogram(t))

t1 = Time(7, 43)
t2 = Time(7, 41)
t3 = Time(7, 37)
total = sum([t1, t2, t3])
print(total)

# Exercises
# 17-1

'''
class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.
        hour: int
        minute: int
        second: int or float
        """
        minutes = hour * 60 + minute
        self.seconds = minutes * 60 + second

    def __str__(self):
        """Returns a string representation of the time."""
        minutes, second = divmod(self.seconds, 60)
        hour, minute = divmod(minutes, 60)
        return '%.2d:%.2d:%.2d' % (hour, minute, second)

    def print_time(self):
        """Prints a string representation of the time."""
        print(str(self))

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        return self.seconds

    def is_after(self, other):
        """Returns True if t1 is after t2; false otherwise."""
        return self.seconds > other.seconds

    def __add__(self, other):
        """Adds two Time objects or a Time object and a number.
        other: Time object or number of seconds
        """
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        """Adds two Time objects or a Time object and a number."""
        return self.__add__(other)

    def add_time(self, other):
        """Adds two time objects."""
        assert self.is_valid() and other.is_valid()
        seconds = self.seconds + other.seconds
        return int_to_time(seconds)

    def increment(self, seconds):
        """Returns a new Time that is the sum of this time and seconds."""
        seconds += self.seconds
        return int_to_time(seconds)

    def is_valid(self):
        """Checks whether a Time object satisfies the invariants."""
        return self.seconds >= 0 and self.seconds < 24*60*60


def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """
    return Time(0, 0, seconds)


def main():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print('Example of polymorphism')
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)


if __name__ == '__main__':
    main()
'''


# 17-2

'''
class Kangaroo:
    """A Kangaroo is a marsupial."""
    
    def __init__(self, name, contents=[]):
        """Initialize the pouch contents.
        name: string
        contents: initial pouch contents.
        """
      
        self.name = name
        self.pouch_contents = contents

    def __init__(self, name, contents=None):
        """Initialize the pouch contents.
        name: string
        contents: initial pouch contents.
        """
        
        self.name = name
        if contents == None:
            contents = []
        self.pouch_contents = contents

    def __str__(self):
        """Return a string representaion of this Kangaroo.
        """
        t = [ self.name + ' has pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """Adds a new item to the pouch contents.
        item: object to be added
        """
        self.pouch_contents.append(item)


kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
print(roo)
'''











