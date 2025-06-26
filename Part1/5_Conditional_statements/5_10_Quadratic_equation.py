from math import sqrt

a = int(input("Value of a: "))
b = int(input("Value of b: ")) 
c = int(input("Value of c: "))

x_positive = (-b + sqrt(b * b - 4 * a * c)) / ( 2 * a)
x_negative = (-b - sqrt(b * b - 4 * a * c)) / ( 2 * a)

print(f"The roots are {x_positive} and {x_negative}")