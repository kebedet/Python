# a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character
def findCharacters(word_list, char):
    output = []
    for word in word_list:
        for w in word:
            if w == char:
                output.append(word)
                break
    new_list = output
    print new_list

findCharacters(['hello','world','my','name','is','Anna'], "o")