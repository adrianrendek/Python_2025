number_of_students = int(input("How many students on the course? "))
groups_to_form = int(input("Desired group size? "))
if ((number_of_students // groups_to_form) * groups_to_form) < number_of_students:
    print(f"Number of groups formed: {(number_of_students // groups_to_form) + 1}")
else:
    print(f"Number of groups formed: {number_of_students // groups_to_form}")