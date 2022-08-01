MINIMUM_CHARACTERS= 10
password = input("Enter password of at least 10 characters :")
while len(password) < MINIMUM_CHARACTERS:
    print("Password does not meet requirements")
    password = input("Enter password of at least 10 characters :")
print ("*" * len(password))