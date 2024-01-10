#blank list...

# users = [] #empty list
# print(users)
# print(type(users))

users = ["amit","sumit","ram","shyam","mike","jane","tom","jerry"]
print(users)

# for i in range(0,len(users)):
#     print(users[i])

# for i in users:
#     print(i)

#print(users[0])

users.append("ayush")
users.insert(2,"raj")
print(users)


#removedelm = users.pop() #it will remove last element
removedelm = users.pop(2)
print("removing..",removedelm)
print(users)

users.remove("jane")
print(users)


#users.extend(["priya","rama","sushma"])
users.extend("priya")
print(users)


