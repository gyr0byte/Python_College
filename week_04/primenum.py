num = int(input("Enter you number: "))
if num <= 0:
    print(f"The Number cannot be 0 or Negative.")

elif num%2 == 0 and num%3 == 0:
    print(f"The Number is not a Prime.")

else:
    print(f"The Number is a Prime")