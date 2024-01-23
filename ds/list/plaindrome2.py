data =[121,222,345,65,78]

x = []
for i in data:
    if str(i) ==(str(i)[::-1]):
        x.append(i)

print(x)      
print(type(x[0]))  
        