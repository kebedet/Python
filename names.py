def display_array(arr):
    for element in range(len(arr)):
        dic = arr[element]
        print dic["first_name"], " " , dic["last_name"]

students = [
{'first_name' : 'Michael', 'last_name' : 'Jordan'},
{'first_name' : 'John', 'last_name' : 'Rosales'},
{'first_name' : 'Mark', 'last_name' : 'Guillen'},
{'first_name' : 'KB', 'last_name' : 'Tonel'}
]

display_array(students)

def display_array_dic(arrDic):
    for key , value in arrDic.items():
        if key == "Students":
            print "Students"
        else:
            print "Instructors"
        arr = value
        for element in range(len(arr)):
            dic = arr[element]
            print element + 1, "-", dic["first_name"],  dic["last_name"], "-", len(dic["first_name"]) + len(dic["last_name"]) 

students = [
{'first_name' : 'Michael', 'last_name' : 'Jordan'},
{'first_name' : 'John', 'last_name' : 'Rosales'},
{'first_name' : 'Mark', 'last_name' : 'Guillen'},
{'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
display_array_dic(users)