#display star for given lists
def display_star(arr1):

    star = "*"
    for element in range(len(arr1)):
        if(type(arr1[element])==int):
            print star * arr1[element]
        else:
            string = arr1[element]
            print string[0] * len(string)

display_star( [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])