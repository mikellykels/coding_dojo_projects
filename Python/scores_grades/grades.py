import random

'''
Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D Score: 70 - 79; Grade - C Score: 80 - 89; Grade - B Score: 90 - 100; Grade - A
'''

def grades(reps):
    print "Scores and Grades"
    for x in range(0, reps):
        score = random.randint(60, 100)
        if score >= 60 and score <= 69:
            print "Score: {}. Your grade is a D.".format(score)
        elif score >= 70 and score <= 79:
            print "Score: {}. Your grade is a C.".format(score)
        elif score >= 80 and score <= 89:
            print "Score: {}. Your grade is a B.".format(score)
        elif score >= 90 and score <= 100:
            print "Score: {}. Your grade is a A.".format(score)
        else:
            print "Unfortunately, you failed"
    print "End of program. Bye!"

grades(10)
