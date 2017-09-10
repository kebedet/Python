#print even and odd numbers
def odd_even():
    for i in range(2001):
        if(i%2==0):
            print "Number is " + str(i) + ". This is an even number"
        else:
            print "Number is " + str(i) + ". This is an odd number"
  
odd_even()

#print the list by multiplying by n
def list_Multiplier(arr, n):
    new_arr = []
    for element in range(len(arr)):
        new_arr.append(arr[element]*5)
    return new_arr

print list_Multiplier([2,4,10,16], 5)

#Hacker challenge
def layered_multiplier(arr):
    new_arr=[]
    inner_arr=[]
    for element in range(len(arr)):
        inner_arr=[]
        for i in range(arr[element]):
            inner_arr.append(1)
        new_arr.append(inner_arr)
    print new_arr

layered_multiplier(list_Multiplier([1,4,3,2], 2))