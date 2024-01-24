keys = [1,2,3,4,5]
data ={}

for i in keys:
    value = input("Enter value: ")
    data.update({i:value})
# for i in range(len(keys)):
#     value = input("Enter value: ")
#     data.update({keys[i]:value})

print(data)    
    
    