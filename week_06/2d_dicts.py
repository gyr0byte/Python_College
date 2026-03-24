n = int(input("Enter how many students you want to enter: "))
d = {}

for i in range(n):
    name = input("Enter the name of the student: ")
    d[name] = {}  
    
    for j in range(5):
        subject = input(f"Enter the name of subject {j+1}: ")
        marks = int(input(f"Enter the marks of subject {j+1}: "))
        d[name][subject] = marks

print(d)