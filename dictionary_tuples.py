def dictionary_in_tuple_out(dic):
    arr = []
    for key, value in dic.items():
        string = key,  value
        arr.append(string)
    print arr

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

dictionary_in_tuple_out(my_dict)