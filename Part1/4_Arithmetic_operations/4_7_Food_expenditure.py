eating_per_week = int(input("How many times a week do you eat at the student cafeteria? "))
price_of_lunch = float(input("The price of a typical student lunch? "))
groceries_per_week = float(input("How much money do you spend on groceries in a week? "))

print("Average food expenditure: ")
print(f"Daily: {(eating_per_week * price_of_lunch + groceries_per_week) / 7 } euros")
print(f"Weekly: {eating_per_week * price_of_lunch + groceries_per_week} euros")