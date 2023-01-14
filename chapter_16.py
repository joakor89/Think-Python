# Chapter 16 Classes & functions > Think Python


# Time 

class Time:
    """Represents the time of day.
    
    attributes: hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

# Pure functions

def add_time(t1, t2):
    sum = Time()
    sum. hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum 


start = Time()
start.hour = 9
start.minute = 45
start.second = 0
duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

# done = add_time(start, duration)
# print_time(done)

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

# Modifiers

def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

# Prototyping versus planning

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def add_time(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)


# Exercise
# 15-1

'''
from datetime import datetime

# to avoid duplicating code, I'm importing everything from Time1
from Time1 import *


def is_after(t1, t2):
    """Returns True if t1 is after t2; false otherwise."""
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)


def increment(t1, seconds):
    """Adds seconds to a Time object."""
    assert valid_time(t1)
    seconds += time_to_int(t1)
    return int_to_time(seconds)


def mul_time(t1, factor):
    """Multiplies a Time object by a factor."""
    assert valid_time(t1)
    seconds = time_to_int(t1) * factor
    return int_to_time(seconds)


def days_until_birthday(birthday):
    """How long until my next birthday?"""
    today = datetime.today()
    # when is my birthday this year?
    next_birthday = datetime(today.year, birthday.month, birthday.day)

    # if it has gone by, when will it be next year
    if today > next_birthday:
        next_birthday = datetime(today.year+1, birthday.month, birthday.day)

    # subtraction on datetime objects returns a timedelta object
    delta = next_birthday - today
    return delta.days


def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.
    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """
    assert b1 > b2
    delta = b1 - b2
    dday = b1 + delta
    return dday


def datetime_exercises():
    """Exercise solutions."""

    # print today's day of the week
    today = datetime.today()
    print(today.weekday())
    print(today.strftime('%A'))

    # compute the number of days until the next birthday
    # (note that it usually gets rounded down)
    birthday = datetime(1967, 5, 2)
    print('Days until birthday', end=' ')
    print(days_until_birthday(birthday))

    # compute the day one person is twice as old as another
    b1 = datetime(2006, 12, 26)
    b2 = datetime(2003, 10, 11)
    print('Double Day', end=' ')
    print(double_day(b1, b2))


def main():
    # if a movie starts at noon...
    noon_time = Time()
    noon_time.hour = 12
    noon_time.minute = 0
    noon_time.second = 0

    print('Starts at', end=' ')
    print_time(noon_time)

    # and the run time of the movie is 109 minutes...
    movie_minutes = 109
    run_time = int_to_time(movie_minutes * 60)
    print('Run time', end=' ')
    print_time(run_time)

    # what time does the movie end?
    end_time = add_times(noon_time, run_time)
    print('Ends at', end=' ')
    print_time(end_time)

    print('Does it end after it begins?', end=' ')
    print(is_after(end_time, noon_time))

    print('Home by', end=' ')
    travel_time = 600      # 10 minutes
    home_time = increment(end_time, travel_time)
    print_time(home_time)

    race_time = Time()
    race_time.hour = 1
    race_time.minute = 34
    race_time.second = 5

    print('Half marathon time', end=' ')
    print_time(race_time)

    distance = 13.1       # miles
    pace = mul_time(race_time, 1/distance)

    print('Time per mile', end=' ')
    print_time(pace)

    datetime_exercises()
'''


# 15-2

'''
def main():
    print("Today's date and the day of the week:")
    today = datetime.today()
    print(today)
    print(today.strftime("%A"))

    print("Your next birthday and how far away it is:")
    #s = input('Enter your birthday in mm/dd/yyyy format: ')
    s = '5/11/1967'
    bday = datetime.strptime(s, '%m/%d/%Y')

    next_bday = bday.replace(year=today.year)
    if next_bday < today:
        next_bday = next_bday.replace(year=today.year+1)
    print(next_bday)

    until_next_bday = next_bday - today
    print(until_next_bday)

    print("Your current age:")
    last_bday = next_bday.replace(year=next_bday.year-1)
    age = last_bday.year - bday.year
    print(age)

    print("For people born on these dates:")
    bday1 = datetime(day=11, month=5, year=1967)
    bday2 = datetime(day=11, month=10, year=2003)
    print(bday1)
    print(bday2)

    print("Double Day is")
    d1 = min(bday1, bday2)
    d2 = max(bday1, bday2)
    dd = d2 + (d2 - d1)
    print(dd)
'''

if __name__ == '__main__':
    pass




















