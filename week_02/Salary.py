name = input("Enter the name of the employee")
salary = int (input("Enter the basic salary of the employee"))

print("=========Salary Slip=========\n")
print("Allowance: ", 0.1*salary)
print("Tax: ", 0.05*salary)
print("Net Salary: ", salary + ((0.1*salary) -  (0.05*salary)))