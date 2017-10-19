


2 == 3 # False
3 == 3 # True
2 != 3 # True
4 >= 3 # True
4 <= 3 # False

# if statements

# If (condition):
#       code..

if True:
    print("It worked")

num1 = 300
num2 = 300

if num1 < num2:
    print("num1 is less than num2")
elif num2 < num1:                   # can have numerous elif
    print("num2 is less than num1")
else:
    print("Both numbers are equal")


num1 = 2012
num2 = 2013

if num1 > num2: # Replace CONDITION1 with a valid condition that makes this work
    print("num1 is bigger than num2")

elif num1 == num2: # Replace CONDITION2 with a valid condition that make this work
    print("num1 is equal to num2")
    
elif num1 < num2: # Replace CONDITION3 with a valid condition that make this work
    print("num2 is bigger than num1")


# Logical Operators

C = 10
D = 5

if C > 10 and D >1:
    print("it worked")

if not(C > 10 and D >1):
    print("it worked")

    
