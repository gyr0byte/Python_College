lst = []
def read(path):
    with open(path, "r") as file:
        for line in file:
            lst.append(line.strip().split(", "))
    print(lst)

read("./week_09/data.txt")