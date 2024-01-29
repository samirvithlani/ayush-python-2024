#{1:1,2:2,3:3,4:4}
#{1:1,2:8,3:3,4:4}

data = {i:i**3 for i in range(1,6)}
print(data)


x = [10,20,30,40,50] #{1:10,2:20,3:30,4:40,5:50}

#data1 = {i:i for i in x}
data1 = {i:x[i-1] for  i in range(1,len(x)+1)}
print(data1)


name = "python"

#data2 = {i:name[i-1] for i in range(1,len(name)+1)}
data2 = {i:i for i in name}
print(data2)
#p:p,y:yy,t:ttt,h:hhhh,o:ooooo,n:nnnnnn

#data3 = {i:name[i-1]*i for i in range(1,len(name)+1)}
#print(data3)

#like this = {p:p:y:yy:t:ttt:h:hhhh:o:ooooo:n:nnnnnn}
#key should also be a string
# 1 --> 6
# name[1-1] name[0] ="p" : p*1
data3 = {name[i-1]:name[i-1]*i for i in range(1,len(name)+1)}
print(data3)

#data3 = {i:name[i] for i in range(1,len(name)+1)}
#print(data3)




