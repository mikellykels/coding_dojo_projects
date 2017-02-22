# Find and replace: print the position of the first instance of the word "monkey". Then create a new string where the word "monkey" is replaced with the word "alligator".

str = "If monkeys like bananas, then I must be a monkey!"
print str.find("monkey")
print str.replace("monkey", "alligator")

# Min and Max: Print the min and max values in a list

x = [2,54,-2,7,12,98]
print max(x)
print min(x)

# First and Last: Print the first and last values in a list. Now create a new list containing only the first and last values in the original list.

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0]
print x[len(x)-1]
y = []
y.append(x[0])
y.append(x[len(x)-1])
print y

# New List: Start with a list like this one: x = [19,2,54,-2,7,12,98,32,10,-3,6]. Sort your list first. Then, split your list in half. Push the list created from the first half to position 0 of the list created from the second half.

x = [19,2,54,-2,7,12,98,32,10,-3,6]

x.sort()
print x
first_list = x[0:len(x)/2]
second_list = x[len(x)/2:len(x)-1]
print second_list.insert(0,first_list)
