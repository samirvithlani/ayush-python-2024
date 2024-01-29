#data = {} #dictionary
data = set({100,20,30,90,40,67,8,123}) #set
print(type(data))
print(data)

data.add(200)

print(data)
data.update([90,91])
data.update((78,79))
data.update({80,81})
data.update("abc")
print(data)
data.update(["amit"])
print(data)

# for i in data:
#     print(i)