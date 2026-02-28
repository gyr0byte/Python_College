p1 = int(input("Enter the price of the product 1: "))
p2 = int(input("Enter the price of the product 2: "))
p3 = int(input("Enter the price of the product 3: "))
p4 = int(input("Enter the price of the product 4: "))

subtotal = p1+ p2+ p3+ p4
discount = 0.05* subtotal
finalamount = subtotal-discount

print("====== Receipt ======")
print("Sub Total: ", subtotal)
print("Discount provided: ", discount)
print("Final Cost: ", finalamount)