# Part I: Create a function called draw_stars() that takes a list of numbers and prints out *.

def draw_stars(arg):
    for x in arg:
        stars = "*"
        print x * stars

draw_stars([3, 2, 5, 10, 6])

# Part II: Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.

def draw_stars2(arg):
    for x in arg:
        stars = "*"
        if type(x) == int:
            print x * stars
        else:
            print x[:1].lower() * len(x)

draw_stars2([3, "Kelly", 5, "Mikaela", 6])
