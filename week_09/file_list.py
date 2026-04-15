def write(path):
    with open(path, "w") as file:
        data = file.write(
            "ID001, Harry, 85\nID002, Bob, 78\nID003, Shyam, 92")


def read(path):
    lst = []
    with open(path, "r") as file:
        for line in file:
            lst.append(line.strip().split(", "))
    return lst

def add(data, sid, name, mark):
    data.append([sid, name, mark])

def update(data):
    id = input("Enter a ID: ")
    found = False
    for i in data:
        if id == i[0]:
            found = True
            try:
                mark = input("Enter a marks: ")
                i[2] = mark
                print("Update Successful!")
            except:
                print("Enter a numeric value")
    if not found:
        print("id not found!")