name = input("What is your name? ")
n = int(input("How many numbers will you like to input? "))
marks = []
for i in range(n):
    m = int(input(f"Enter the {i+1} subject marks"))
    marks.append(m)
    
highest = marks[0]
lowest = marks[0]
totalmarks = 0
for mark in marks:
    if highest < mark:
        highest = mark
    elif lowest > mark:
        lowest = mark
    totalmarks += mark                     

average = totalmarks / n

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"