no = int(input("Enter a number: "))
ans = 1

for i in range(1,no+1):
    
    ans = ans * i #1 = 1 * 1 ans = 1
                  # 1 = 1 * 2 ans = 2
                  # 2 = 2 * 3 ans = 6
                  # 6 = 6 * 4 ans = 24
                  # 24 = 24 * 5 ans = 120  


print("Factorial of",no,"is",ans)    
    