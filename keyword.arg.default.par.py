
# keyword arguments and default parameters

def about(name,age,likes):
    sentence = "Meet {}! I am {} years old and I like {}".format(name,age,likes)
    return sentence

about("Jack", 23, "Python")


# packing and unpacking using *args and *kwargs

print(1,2,3,4,5)

numbers = [1,2,3,4,5]

# to unpack use "*"

print(*numbers)

# how to pack numbers

def add(x,y):
    return x + y

# lets pack in numbers

def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number # remember 'int' and 'tuple' cannot be added here 
    return(total)

# what about for keyword arguments

# using ** arguments 

def about(name,age, likes):
    sentence = "Meet {}! I am {} years old and I like {}".format(name,age,likes)
    return sentence

dictionary = {"name": "Django", "age": 23, "likes": "Python"}

about(**dictionary)

# now using *kwargs

def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key,value))
