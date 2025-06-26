houry = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day = input("Day of the week: ")
if day == "Sunday":
    print(f"Daily wages: {houry * 2 * hours_worked} euros")
else:
    print(f"Daily wages: {houry * hours_worked} euros")