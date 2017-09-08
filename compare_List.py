#a function used to check two lists are identical or not.
def compare_List(List1, List2):
    list1 = List1
    list2 = List2
    if set(list1)==set(list2):
        print "The lists are  the same"
    else:
        print "The list are not the same"


compare_List(['celery','carrots','bread','milk'], ['celery','carrots','bread','cream'])