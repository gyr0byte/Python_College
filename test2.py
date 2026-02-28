'''a = int (input("Enter your first number"))
b = int (input("Enter your second number"))
temp = a
a = b
b = temp
print("The swapped values are")
print(a)
print(b) '''

item1 = input("Enter the name of item 1")
itemp1 = int (input("Enter the price of item 1"))
item2 = input("Enter the name of item 2")
itemp2 = int (input("Enter the price of item 2"))
item3 = input("Enter the name of item 3")
itemp3 = int (input("Enter the price of item 3"))

totalcost = itemp1 + itemp2 + itemp3
taxitem1 = 0.13 * itemp1
taxitem2 = 0.13 * itemp2
taxitem3 = 0.13 * itemp3

finalcost1 = itemp1 - taxitem1
finalcost2 = itemp2 - taxitem2
finalcost3 = itemp3 - taxitem3
print("======= Receipt =======")
print(item1, ": Rs", itemp1)
print(item2, ": Rs", itemp2)
print(item3, ": Rs", itemp3)
print("=======================")
print("Total Cost: ", totalcost, "\nTax: ", taxitem1+taxitem2+taxitem3, "\nFinal Cost: ", finalcost1+finalcost2+finalcost3)

