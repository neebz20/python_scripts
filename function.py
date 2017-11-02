
# functions

  # can call arbitrary parameters such as "x" and "y" anything else- i.e. "astros" and "texans"

def add(x,y):
       return x + y   # returning values is not the same as printing values
answer = add(5,7)
answer

# new challenge

# create a function called "rev"
def rev(text):                      # take in a parameter called "text"
    return text[::-1]
reverse = rev("California").lower()


# scopes

# 2 types of scopes - "global" and "local"
