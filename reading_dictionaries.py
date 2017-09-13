personInfo = {"name":"kebede","age":42, "birth":"Addis Ababa", "language":"Python"}
print "My name is: " , personInfo["name"] , "\nMy age is: " , personInfo["age"] , "\nMy country is " + personInfo["birth"] , "\nMy favorite language is " , personInfo["language"]

#prints key and value of any dictionary
def display_key_value(dic):
    for key , value in dic.items():
        print key, " " , value 
display_key_value(personInfo)