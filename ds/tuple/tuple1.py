data = ("John", "amit","Doe", 53.44,"amit")
print(data)
print("type of data: ", type(data))

x = data.count("amit")
print("count of amit: ", x)

ind = data.index("amit")
print("index of amit: ", ind)

print(data[0])
data[0] = "amit"