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
    
    