bonus_points = int(input("How many points are on your card?: "))
if bonus_points < 100:
    print(f"Your bonus is 10%")
    print(f"You now have {bonus_points * 1.1} points")
if bonus_points >= 100:
    print(f"Your bonus is 15%")
    print(f"You now have {bonus_points * 1.15} points")