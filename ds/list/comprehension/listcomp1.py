data = [10,20,30,40,50,60]
# data1 =[]

# for i in data:
#     data1.append(i+10)

# print(data1)    

data1 = [i+10 for i in data]
print(data1)

data2 =[i for i in data if i > 40]
# for i in data:
#     if i >40:
#         data2.append(i)

print(data2)        