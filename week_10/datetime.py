import datetime as dt 

# Get the current date and time
def file_create():
    now = dt.datetime.now()
    print("Current date and time:", now)

    # Create a filename with the current date and time
    filename = now.strftime("file_%Y-%m-%d_%H-%M-%S.txt")
    print("Generated filename:", filename)

    # Create a file with the generated filename
    with open(filename, 'w') as file:
        file.write("This file was created on " + now.strftime("%Y-%m-%d at %H:%M:%S"))

print(file_create())
