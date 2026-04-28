from datetime import datetime


def file_create():
    user_name = input("Enter your name: ")
    now = datetime.now()
    with open(f"{user_name}_{now.year}{now.month}{now.day}_{now.hour}{now.minute}{now.second}.txt", "w") as file:
        file.write("This is a uniquely created file")

print(file_create())
