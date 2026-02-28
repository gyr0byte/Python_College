import math
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
discriminant = b**2 - 4*a*c
xp = (-b + math.sqrt(discriminant))/ (2*a)
xn = (-b - math.sqrt(discriminant))/ (2*a)
print("The Negative value of x is ",xp)
print("The Positive value of x is ",xn)