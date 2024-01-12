users = ["amit","zara","parth","priya","sumit","priya"]

cnt = users.count("priya")
print(cnt)



# ind = users.index("parth")
# print(ind)

name = input("enter name to search:")

if users.count(name)>0:
    ind = users.index(name)
    print(ind)
else:
    print("not found")


