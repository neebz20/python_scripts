
# scopes

# 2 types of scopes - "global" and "local"

a = 300         # global 

def f1():
    b = a + 20  # local 
    print(b)

def f2():
    a = 50      # local 
    print(a)

f1()
f2()
print(a)


# How to overwrite a global value inside a function
# use global keyword

a = 175

def f1():
    global a   # global
    a = 125
    print(a)

def f2():
    a = 50     # local 
    print(a)

f1()
f2()
print(a)


# altering scopes which are sets

a = [1,2,3]    #global

def f1():
    a[0] = 2   # did not have to insert a global command to alter previous global command
    print(a)

def f2():
    a = 50     # local 
    print(a)

f1()
f2()
print(a)
