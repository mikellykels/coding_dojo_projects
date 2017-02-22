import random

# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.

def coin_toss():
    print "Starting the program..."
    heads = 0
    tails = 0
    for x in range(0, 51):
        toss = random.randint(1, 2)
        if toss == 1:
            heads += 1
            print "Attempt #{}: Heads! Got {} head(s) so far and {} tail(s) so far.".format(x, heads, tails)
        else:
            tails += 1
            print "Attempt #{}: Tails! Got {} head(s) so far and {} tail(s) so far.".format(x, heads, tails)
    print "End of program. Thanks!"

coin_toss()
