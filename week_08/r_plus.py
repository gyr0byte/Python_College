with open("week_08/file.txt", "r+") as file:
    data = file.read()
    print(data)
    file.seek(0)
    file.write("Start")
