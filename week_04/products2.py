choice = True
subtotal = 0
while choice==True:
    name = input("Enter the name of the product: ")
    price = int(input("Enter the price of the product: "))
    user = input("Do you want to enter more products? (yes/no): ")
    if (user.lower() == "no"):
        choice = False
    if price <= 0:
        continue
    else:
        subtotal += price
        
totalamt = subtotal + (0.13*subtotal)
deliver = input("Do you want to deliver the product (Yes/No): ")
if deliver == "yes":
    totalamt += 100
    
print(f"The Total Cost is: Rs{totalamt}")