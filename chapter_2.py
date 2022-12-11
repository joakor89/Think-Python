# Think Python > chapter 2 > Variables, expressions & statements
# this was performed directly at Visual studio code
# Nevertheless; On this book it's performed directly from Python or console IDE 

message = 'And now for something completely different'
print(message)
n = 17
print(n)
pi = 3.141592653589793
print(pi)

# variable names


'''
These are examples of hwo not to define a variable
all of them will drop a SyntaxError

'76trombrones = "big parade" '
more@ = 1000000
clas = 'Advance theorical zymurgy
'''

# Expression & statements

print(42)
print(n)
print(n + 25)

n = 17
print(n)

# Script mode 
miles = 26.2
route = miles * 1.61
print(route)
# Also, can be done by
print(miles * 1.61)
print(1)
x = 2
print(x)
x = 5 
print(x + 1)

# Order of operations 
# Python follows PEMDAS convention
'''
Parentheses
Exponentation
Multiplication and division 
Addition and subtraction
'''

# string operations 

'''
The following are considered illegal
"2" - "1"   'eggs' / 'easy'     'third'*'a charm'
'''

first = 'throat '
second = 'warbler'
print(first + second)

minute = 60
percentage = (minute * 100) / 60
print(percentage)

x = y =1
print(x)


# Exercise
'''
2-1.1
42 = n will collide with python convetions. Python used to read the chuck code
from left to right. Also, it is a guidance that variables assigned from left to right.
Allocating the 42 first violates the convention and then, python report an invalid syntax error

2-1.2
In this case the value assigned to variable "y" was stored within x variable
there is no issue on it
2-1.3
Indates separation instead of termination of 
2-1.4
dots are related with function extantion or invocation, python will interpreted
this as missing syntax to fill and will report and error
2-1.5
Since are not defined, python will firstly report an syntax error
then, it will report a Runtime error if user decided to ignore it



'''
# # Exercise 2-2.1
# pi = 3.141592   # Pi representation
# r = 5           # Radius value
# # Since the formula presented in the book shown a division. I rather apply float numbers to it
# # Then, the outcome will be
# answer = 4.0 / 3.0 * pi * r**3
# print(answer)

# Exercise 2-2.2
total_books = 60
cover_price = 24.95   
disc_x_books = 9.98    
af_disc = 14.97
fs_cost_deliv = 3
total_fb = af_disc + fs_cost_deliv
print(total_fb)
# First book will totally cost 17.97
total_fb = 17.97

#Lets calculate the rest
second_deliv_disc = 0.75                        # Second delivery offer for remaining books
snd_book_offer = af_disc + second_deliv_disc    # book after discount plus second delivery offer
print(snd_book_offer)                           # second total price for remaining books

remaining_books = 59                                # remaining books
remaining_send = snd_book_offer * remaining_books   # second prince multiplied by remainig books
print(remaining_send)                               # total price for the rest of the books
















