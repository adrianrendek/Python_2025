pin_set = 4321
pin_attempt = 0
pin_to_find = 0

while pin_to_find != pin_set:
    pin_to_find = int(input("PIN: "))
    pin_attempt += 1
    if pin_to_find == pin_set:
        break
    else:
        print("Wrong")

if pin_attempt == 1:
    print(f"Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {pin_attempt} attempts")