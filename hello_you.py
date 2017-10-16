

# Ask user for name

name =input("What is your name?: ")
print(name)
print(type(name))

# Ask user for age

age = input("How old are you?: ")
print(age)
print(type(age))

# Ask user for city

city = input("What city do you live in?: ")
print(city)


# Ask user what they enjoy

love = input("What do you love doing?: ")
print(love)


# Create output text
string = "Your name is {} and you are {} years old. You live in {} and love {}."
output = string.format(name, age, city, love)

# Print output to screen

print(output)


A = "part"
B = 1

print(A + str(B))

# Using format function
"{}-{}".format(A,B)

# Reverse format
"{1}-{0}".format(A,B)


#Practice 1

# First, create a variable called start, and set it equal to "I am ".
# Remember the space after the word "am" !
start = "I am "

# Next, create a variable called age and set it equal to your age in years.
# This must be a number
age = int("23")

# Next, create a variable called end, and set it equal to " years old".
# Remember the space before the word "years"
end = " years old"

# Next, create a variable called output, and use the format() function to add
# together the start, age and end variables. 
string = "{}{}{}"
output = string.format(start, age, end)
# An example output string would be "I am 15 years old"

# Finally, print the output to the screen using the print() function.

print(output)


#Practice 2

# Create a variable called name and set it equal to your name
name = "David"

# Create a variable called age and set it to your age in years 
# Note: This must be an int, not a string!
age = int(23)

# Create a variable called place and set it equal to where you live
place = "Texas"

# Create a variable called output, and use string formatting to 
# make it like the example text in the description
string = "Hello my name is {} and I am {} years old. I live in {} and I love Python!"
output = string.format(name, age, place)
# Finally, use the print() function to print the output
print(output)
