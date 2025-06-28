grades = int(input("How many points [0-100]: "))
if grades > 100 or grades < 0:
    print("Grade: impossible!")
elif grades <= 100 and grades >= 90:
    print("Grade: 5")
elif grades <= 89 and grades >= 80:
    print("Grade: 4")
elif grades <= 79 and grades >= 70:
    print("Grade: 3")
elif grades <= 69 and grades >= 60:
    print("Grade: 2")
elif grades <= 59 and grades >= 50:
    print("Grade: 1")
elif grades <= 49 and grades >= 0:
    print("Grade: fail")