name = input("Enter your name: ")
recharge = int(input("Enter the Recharge amount: "))
tax = 0.1*recharge
totalpay = recharge + tax
print("====== Recharge Detail ======")
print("Recharge Amount: ", recharge)
print("Tax Amount: ", tax)
print("Total Cost: ", totalpay)