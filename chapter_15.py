# Chapter 15 Classes & objects > Think python
import math
import copy
import turtle


# Programmer-defined types
'''
a programmer-defined type it's also called class
it looked like this:

'''

class Point:
    """Repreents a point in 2-D space."""

print(Point)
blank = Point()
print(blank)

# Attributes
'''
assigning values to named elements of an
object. These elements are called attributes
'''

blank.x = 3.0
print(blank.x)
blank.y = 4.0
print(blank.y)
x = blank.x
print(x)

print('(%g, %g)' % (blank.x, blank.y))
distance = math.sqrt(blank.x**2 + blank.y**2)
print(distance)

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

print_point(blank)

# Rectangles

class Rectangle:
    """Represents a rectangle.
    
    attributes: width, height, corner.
    """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

# Instances as return values

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

center = find_center(box)
print_point(center)

# Objects are Mutable

box.weight = box.width + 50
box.height = box.height + 100

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

print(box.width, box.height)
grow_rectangle(box, 50, 100)
print(box.width, box.height)

# Copying 
p1 = Point()
p1.x = 3.0
p1.y = 4.0
p2 = copy.copy(p1)
print(print_point(p1))
print(print_point(p2))
print(p1 is p2)
print(p1 == p2)

box2 = copy.copy(box)
print(box2 is box)
print(box2.corner is box.corner)

box3 = copy.deepcopy(box)
print(box3 is box)
print(box3.corner is box.corner)

# Exercise 
# 15-1

'''
from Point1 import Point, Rectangle, print_point
from Point1_soln import distance_between_points


class Circle:
    """Represents a circle.
    Attributes: center, radius
    """


def point_in_circle(point, circle):
    """Checks whether a point lies inside a circle (or on the boundary).
    point: Point object
    circle: Circle object
    """
    d = distance_between_points(point, circle.center)
    print(d)
    return d <= circle.radius


def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.
    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x += rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.height
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.
    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    return False


def main():
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()
'''


# 15-2

'''
import polygon

def draw_circle(t, circle):
    """Draws a circle.
    t: Turtle
    circle: Circle
    """
    t.pu()
    t.goto(circle.center.x, circle.center.y)
    t.fd(circle.radius)
    t.lt(90)
    t.pd()
    polygon.circle(t, circle.radius)


def draw_rect(t, rect):
    """Draws a rectangle.
    t: Turtle
    rect: Rectangle
    """
    t.pu()
    t.goto(rect.corner.x, rect.corner.y)
    t.setheading(0)
    t.pd()

    for length in rect.width, rect.height, rect.width, rect.height:
        t.fd(length)
        t.rt(90)


if __name__ == '__main__':
    bob = turtle.Turtle()

    # draw the axes
    length = 400
    bob.fd(length)
    bob.bk(length)
    bob.lt(90)
    bob.fd(length)
    bob.bk(length)

    # draw a rectangle
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    draw_rect(bob, box)

    # draw a circle
    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0

    draw_circle(bob, circle)

    # wait for the user to close the window
    turtle.mainloop()
'''



















