#lambda with loop
#x = lambda x : for i in range(1,11): print(x,"*",i,"=",x*i)

def checkName(name):
    flag = True
    for i in name:
        if " " in i:
            flag = False
            break
        
    return flag    
            


isValid = lambda name:checkName(name)
print(isValid("Raj-Kumar"))

