data =[121,222,345,65,78]
x = []
rev =0
sum =0
rem =0
tempno =0
for i in data:
    tempno = i
    while i>0:
        rem = i%10
        rev = rev*10+rem
        i = i//10
    
    print(rev)   
    if rev == tempno:
      x.append(rev) 
    rev =0

    

print(x)    
    
    