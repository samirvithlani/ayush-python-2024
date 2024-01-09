no = int(input("Enter a number: "))
ans = 1

#no =5
for i in range(no,0,-1):
    #i = 5 
    #1 = 1 * 5 ans = 5
    #5 = 5 * 4 ans = 20
    #20 = 20 * 3 ans = 60
    #60 = 60 * 2 ans = 120
    #120 = 120 * 1 ans = 120
    ans = ans * i


print("Factorial of",no,"is",ans)    
    
