
for number in range(1,11):
    print(number)

# calculating the number of vowels and consonants in a given word

vowels = 0
consonants = 0

for letter in "Hello":
    if letter.lower() in "aeiou":
        vowels = vowels +1
    elif letter == " ":
        pass
    else:
        consonants = consonants +1
print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))


# Students

students = {
    "male":["Tom","Charlie", "Harry", "Frank"],
    "female":["Sarah", "Huda", "Samantha", "Emily", "Elizabeth"]
    }

for key in students.keys():
    print(students[key])
