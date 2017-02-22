# Odd/Even: Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

# def odd_even():
#     for num in range(1, 2001):
#         if num % 2 == 0:
#             print "Number is {}. This is an even number.".format(num)
#         else:
#             print "Number is {}. This is an odd number.".format(num)
#
# odd_even()

# Multiply: Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

def multiply(a, b):
    e = []
    for c in a:
        d = c * b
        e.append(d)
    print e

multiply([2, 4, 10, 16], 5)
