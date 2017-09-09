#print multiplication table
num = [1,2,3,4,5,6,7,8,9,10,11,12]
horizontal= ""
space = " "
newline= "\n"
n = 13
for element in num:
    #print element
    for i in range(1, n):
        horizontal= horizontal + str(element * i) + space
    horizontal = horizontal + newline
print horizontal