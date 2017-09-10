import random
def display_grade():
    for i in range(10):
        num =random.randrange(60, 101, 1)
        if(num>=60 and num <=69):
            print "score: " + str(num) + "; your grade is D"
        elif(num>=70 and num <=79):
            print "score: " + str(num) + "; your grade is C"
        elif(num>=80 and num <=89):
            print "score: " + str(num) + "; your grade is B"
        elif(num>=90 and num <=100):
            print "score: " + str(num) + "; your grade is A"
    print  "End of the program. Bye!"

display_grade()