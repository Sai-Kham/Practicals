def main():
    email_to_name = {}
    email = input("Email:  ")
    while email != "":
        prefix = email.split("@")[0]
        parts = prefix.split(".")
        name = " ".join(parts).title()
        check = input("Is your name {}? (Y/n) ".format(name))
        if check.upper() != "Y" and check != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
        for email, name in email_to_name.items():
            print("{} ({})".format(name, email))


main()
