print("Person 1: ")
person_1 = input("Name: ")
person_1_age = int(input("Age: "))
print("Person 2: ")
person_2 = input("Name: ")
person_2_age = int(input("Age: "))

if person_1_age > person_2_age:
    print(f"The elder is {person_1}")
elif person_1_age < person_2_age:
    print(f"The elder is {person_2}")
elif person_1_age == person_2_age:
    print(f"{person_1} and {person_2} are the same age")