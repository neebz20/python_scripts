
# Warm -up before building Travis
L = [1,5,2,6,2,9]
# figure out if 2 is in L
2 in L

# using del command
L = [1,2,3,4,5]
del L[0]

# what if we have two inputs with equivalent value
example = ["A", "B", "C", "A", "B"]
example.remove("A")
print(example) # remove() command removes only the first "A" value

# Remove the second "A" value
del example[3]

# del the first two values
del example[0:2]


# concatenate to a list 
A = [1,22,33,48,75]
A = A +[1]
print(A)

# concatenate a string to list
A = A + ["BCD"]
A = A + list("BCD")

# concatenate an int to list
A = A + [[1,2,3]] 
# or int(s0
A = A + [[1],[2],[3]]

# using insert() to insert '100' between 22 and 33
A.insert(2,100)

# using tuple
our_tuple = 1,2,3,"A","B","C"
A = [1,2,3]
tuple(A)

D,E,F = [1,2,3]
G,H,I = "789"



# Travis, our trusted robot


known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie","Harry"]

print(len(known_users))

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?:").lower()
        if remove == "y":
            known_users.remove(name)
            print(known_users)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")
    else:
            print("Hmmm I don't think I have met you yet") # how to stop a loop: crl c
            add_me = input("What you like to be added to the system (y/n)?: ").strip().lower()
            if add_me == "y":
                print(known_users)
                known_users.append(name) # .append() adds name to known_users
            elif add_me == "n":
                print("No worries, see you around!")

            

        




    
