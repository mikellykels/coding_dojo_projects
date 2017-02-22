# Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

for odd in range(1, 1001, 2):
    print odd

# Create another program that prints all the multiples of 5 from 5 to 1,000,000.

for mult in range(5, 1000005, 5):
    print mult

# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
print sum(a)

# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
avg = sum(a)/len(a)
print avg
