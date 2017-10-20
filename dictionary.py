

students = {}
students = {"Alice":25, "Bob": 27, "Claire": 17, "Dan":21, "Emma":22}

# how to look up a key
students["Dan"]

# New student named Fred
students["Fred"] = 25

# what if Alice just had a birthday
students["Alice"] = 26

# Fred flunked out, bye Fred
del students["Fred"]

# dict_keys
a =list(students.keys())
a[0]
a[2]
# dict_values
students.values()

# dict_ items
students.items()


# new structured dictionary - adding more than one value (studentID, age, letter grade)
students = {"Alice":{"id":"ID0001","age":26,"grade":"A"},
            "Bob":{"id":"ID0002","age":27,"grade":"B"},
            "Claire":{"id":"ID0003","age":17,"grade":"C"},
            "Dan":{"id":"ID0004","age":21,"grade":"D"},
            "Emma":{"id":"ID0005","age":22,"grade":"E"}
            }
# print Claire's information
print(students["Claire"]["age"])

# print Emma's age and letter grade
print(students["Emma"]["id"], students["Emma"]["grade"])









