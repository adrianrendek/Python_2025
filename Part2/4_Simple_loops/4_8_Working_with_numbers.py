print("Please type in integer numbers. Type in 0 to finish.")
number = 1
number_counter = 0
number_sum = 0
mean = 0
is_negative = 0
is_positive = 0 

while number != 0:
    number = int(input("Number: "))
    if number > 0:
        is_positive += 1
    elif number < 0:
        is_negative += 1
    number_sum = number_sum + number
    number_counter += 1
    if number == 0:
        break
print(f"Numbers typed in {number_counter -1}")
print(f"The sum of the numbers is {number_sum}")
print(f"The mean of the numbers is {number_sum / (number_counter -1)}")
print(f"Positive numbers {is_positive}")
print(f"Negative numbers {is_negative}")
