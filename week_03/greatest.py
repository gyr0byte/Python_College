num1 = int (input("Enter your first Number"))
num2 = int (input("Enter your Second Number"))
num3 = int (input("Enter your Third Number"))
if(num1 > num2 & num1>num3):
    print("First number is the greatest")

elif(num2 > num1 & num2 > num3):
    print("Second number is the greatest")

else:
    print("Third number is the greatest")