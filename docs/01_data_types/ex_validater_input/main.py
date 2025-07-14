
# Validate User Input

username = input("Please enter a username")
# Username is no more than 12 chars
if len(username) > 12:
    print ("Username can't be more than 12 chars")
elif not username.find(" ") ==-1:
    print("Username can't contain spaces")
elif username.isalpha() == False:
    print("Username can't contain spaces")
else:
    print(f"Welcome {username}")
