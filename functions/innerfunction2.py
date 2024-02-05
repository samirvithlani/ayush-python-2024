def outer(a,b):
    #10 , 20
    def inner(a,b):
        #20, 30
        return a+b
    
    x = inner(a+10,b+10)
    #10+20, 20 +10 = 30, 30
    return x


ans = outer(10,20)  # No output    
print(ans)  # 40