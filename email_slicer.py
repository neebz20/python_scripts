
# string is an iterable data type
word = "supercalifragilisticexpialidocious"
word[0]
word[2]

# variable[start:end:step]
# end - up to but not including the letter


word[0:5:1] # Gets me "super"

# take out "cali"
word[5:9:1]

# start from cali to the end
word[5:]

# "-" counts from the end
word[-1]

# figure out where "cali using index
word.index("cali")

# take out "cali" using index
word[word.index("cali"):word.index("fragi")]

# take out "docious"
word[word.index("docious"):]



# here is a very long word
word = "antidisestablishmentarianism"

# use a slice to take out the word "establishment"
word[word.index("establishment"): word.index("aria")]

# and store it in the answer variable....
answer = word[word.index("establishment"): word.index("aria")]
print(answer) 








