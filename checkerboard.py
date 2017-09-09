#print checkboard
star = "*"
space = "  "
newline = "\n"
output = ""
n = 0
for i in range(1,65):
    if(i%8==0):
        if(n%2==0):
            output = output + newline + space
        else:
            output = output + newline
        n = n+1
    elif(i%2==0):
        output =  output + space
    else:
        output = output + star

print output