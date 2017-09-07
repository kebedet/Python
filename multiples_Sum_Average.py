#part1 print all the odd numbers from 1 to 1000
for i in range(0,1001):
    if (i % 2 <> 0):
        print i

#partII: print all multiples of 5 from 5 to 1,000,000
for i in range(5, 1000001):
    if(i%5==0):
        print i

#Print the sum of all values in the list a:
a = [1, 2, 5, 10, 255, 3]
output = 0
for element in a:
    output += element

print output

#print the average of the values in the list a:
print output/len(a)