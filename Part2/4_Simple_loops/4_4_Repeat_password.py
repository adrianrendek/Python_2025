password = input("Password: ")
password_2 = ""
while password != password_2:
    password_2 = input("Repeat password: ")
    if password_2 != password:
        print("They do not match!")
print("User account created!")
