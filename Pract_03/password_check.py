
def main():
    MINIMUM_CHARACTERS = 10
    password = get_password(MINIMUM_CHARACTERS)
    print_asterisk(password)

def get_password(MINIMUM_CHARACTERS):
    password = input("Enter password of at least 10 characters :")
    while len(password) < MINIMUM_CHARACTERS:
        print("Password does not meet requirements")
        password = input("Enter password of at least 10 characters :")
    return password

def print_asterisk(password):
    print("*" * len(password))


main()