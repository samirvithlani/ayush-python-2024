data1 = set({"ram","shyam","hari","sita","gita"})
data2 = set({"arjun","shyam","karna","bhim"})

# x = data1.difference(data2)
# print(x)

# x = data1.intersection(data2)
# print(x)

# x = data1.union(data2)
# print(x)

# x = data1.symmetric_difference(data2)
# print(x)

data1.difference_update(data2)
print(data1)