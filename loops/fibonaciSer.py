#0 1 1 2 3 5 8 13 

a = 0
b = 1
c = 0
print(a, end=" ")
print(b, end=" ")
for i in range(1,10):
    #0 = 0 + 1 c =1
    # 1 = 1 + 1 c = 2
    #2 = 1 + 2 c = 3
    #3 = 2 + 3 c = 5
    c = a + b
    print(c, end=" ")
    #a = 1
    #a = 1
    #a = 2
    a = b
    #b = 1
    #b = 2
    #b = 3
    b = c
    
    