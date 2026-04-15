def write(path):
    with open(path, "w") as file:
        data = file.write(
            "ID001, Harry, 85\nID002, Bob, 78\nID003, Shyam, 92")


lst = []


def read(path):
    with open(path, "r") as file:
        for line in file:
            lst.append(line.strip().split(", "))
    print(lst)


path = "./week_09/data.txt"
write(path)
read(path)
