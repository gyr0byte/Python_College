import file_list as fl
path = "./week_09/data.txt"
data = fl.read(path)
print(data)
fl.add(data, "ID004", "Gaurav", "87")
print(data)
