name = input("Enter your name")
unit = int(input("Enter the unit consumed"))
cost = int(input("Enter the cost per unit"))

print("==========Electricity Bill==========\n")
print("Total Bill Amount: ", unit*cost)
print("Total Tax: ", 0.08 * (unit*cost))
print("Final Bill: ", (unit*cost) - (0.08 * (unit*cost)))