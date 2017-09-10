import random
def coin_toss():
    head = 0
    tail = 0
    print "Starting the program..."
    for i in range(1, 5001):
        x = round(random.random())
        if(x==1):
            head = head +1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a head! ... got " + str(head) + " head(s) so far and " + str(tail) + " tail(s) so far"
        else:
            tail = tail + 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a tail! ... got " + str(head) + " head(s) so far and " + str(tail) + " tails(s) so far"
    print "End of the program. Thank you!"

coin_toss()