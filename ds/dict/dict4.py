data = {1:"hindi",2:"malayalam",3:"english",4:"marathi",5:"gujarati"}
#print(data)

# x = data.items()
# print(x)

x = data.keys()
print(x)

x = data.values()
print(x)

# for i,j in data.items():
#     print(i," - ",j)

#need to pass key...
# remvedItem = data.pop(22)
# print(remvedItem)
# print(data)


# remvovedElm = data.popitem()
# print(remvovedElm)
# print(data)

while len(data)>0:
    
    remvedItem = data.popitem()
    print(remvedItem)
    

print(data)