#Assignme: Filter by Type
def compare_Type_Value(data_input):
    if(type(data_input)) == int:
        if(data_input >= 100):
            print "That's a big number!"
        else:
            print "That's a small number."
    elif (type(data_input) == str):
        if(len(data_input)>=50):
            print "Long sentence."
        else:
            print "Short sentence."
    elif (isinstance(data_input, list)):
        if(len(data_input)>=10):
            print "Big list!"
        else:
            print "Short list."
    else:
        print "the input is not Integer or String or List"

compare_Type_Value(['name','address','phone number','social security number'])