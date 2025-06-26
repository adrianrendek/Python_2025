name = input("Please tell me your name: ")
if name == "Jerry":
    print("Next please!")
else:
    portions = int(input("How many portions of soup? "))
    portion = 5.90
    print(f"The total cost is {portions * portion}")
    print("Next please!")