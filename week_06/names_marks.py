students = {}
n = int(input("Enter how many students are there: "))

for i in range(n):
    names = input(f"Enter the name of the {i+1} student: ")
    marks = int(input(f"Enter the marks of the {i+1} student: "))
    students[names] = marks

print(students)
