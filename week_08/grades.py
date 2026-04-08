names = []
marks = []

with open("week_08/grades.txt", "r") as file:
    for data in file:
        if data.strip() == "":
            continue

        line = data.strip()
        values = line.split(",")

print(line)
print(values)
