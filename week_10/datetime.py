import datetime as dt


def file_create():
    now = dt.datetime.now()
    print("Current date and time:", now)


    filename = now.strftime("file_%Y-%m-%d_%H-%M-%S.txt")
    print("Generated filename:", filename)

    with open(filename, 'w') as file:
        file.write("This file was created on " +
                   now.strftime("%Y-%m-%d at %H:%M:%S"))


file_name = "./week_10/"
print(file_create())
