username = input( "Enter your username")
if len(username)> 12:
    print ("usernme cannot be more than 12 characters")
elif not username.find(" ") ==-1:
    print ("Your username cannot contain spaces")
elif not username.isalpha():
    print("Your username cannot contain digits")
else:
    print(f"Your are welcome {username}")

