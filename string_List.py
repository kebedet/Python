#string and List Practice

words = "It's thanksgiving day. It's my birthday, too!"
str = "day"
print words.find(str)
print words.replace("day", "month")

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]

x_new =[x[0], x[len(x)-1]]
print x_new

x = [19,2,54,-2,7,12,98,32,10,-3,6]
half = (len(x))/2
y =[ x[:(len(x)-1)/2],x[(len(x))/2:]]
print y