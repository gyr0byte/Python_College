print("Welcome to the program!!")
print("======================")


while True:
    print("""
      1. View Data
      2. Add Data
      3. Delete Data
      4. Exit
      """)
    choose = int(input("Enter the option you want to choose: "))
    if choose == 1:
        print("You choosed the view data option!")

    elif choose == 2:
        print("You choosed the Add data option!")

    elif choose == 3:
        print("You choose the Delete data option!")

    elif choose == 4:
        print("Have a nice day!")
        break

    else:
        print("Please choose an valid option")
