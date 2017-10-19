
# get user email address
email = input("What is your email address?: ").strip()

# slice out user name
user = email[:email.index("@"):1]

# slice domain name
domain = email[email.index("@")+1::1]
# format message
output = "your username is {} and your domain is {}.".format(user,domain)


# display output message
print(output)
