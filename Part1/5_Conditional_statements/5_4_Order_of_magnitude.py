number = int(input("Please type in a number: "))
if number < 1000 and number > 100 and number > 10:
    print("This number is smaller than 1000")
    print("Thank you!")
if number < 100 and number < 1000 and number > 10:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("Thank you!")
if number < 10 and number < 100 and number < 1000:
    print("This number is smaller than 1000")
    print("This number is smaller than 100")
    print("This number is smaller than 10")
    print("Thank you!")
elif number > 1000:
    print("Thank you!")