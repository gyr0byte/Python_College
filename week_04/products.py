choice = True
myproduct = []
while choice==True:
    name = input("Enter the name of the product: ")
    price = int(input("Enter the price of the product: "))
    myproduct.append(name)
    myproduct.append(price)
    user = input("Do you want to enter more products? (yes/no): ")
    if (user == "no"):
        choice = False

