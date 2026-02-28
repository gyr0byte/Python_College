principal = int(input("Enter the principal: "))
rate = float(input("Enter the rate: "))
time = int(input("Enter time in yrs: "))
simpleInterest = (principal*time*rate) / 100
totalAmount = principal + simpleInterest

print("Simple Interest: ", simpleInterest)
print("Total Amount: ", totalAmount)