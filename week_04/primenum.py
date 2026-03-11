def pn(num):
    if num < 1:
        print(f"The Number cannot be Negative or Zero")

    for i in range(2,num):
        if(num%i==0):
            print("The Number is not a Prime.")
            break
    
    else:
        print(f"The Number is a Prime.")
    
num = int(input("Enter your Number: "))
pn(num)