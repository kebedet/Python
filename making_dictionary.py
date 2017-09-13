def array_in_dictionary_out(arr1, arr2):
    new_dic = {}
    new_dic = zip(arr1,arr2)
    print dict(new_dic)

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas", "shark"]
array_in_dictionary_out(name, favorite_animal)