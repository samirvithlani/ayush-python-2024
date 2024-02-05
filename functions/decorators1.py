#decorators are use for change behaviour of function without changing the function itself
#decorators denoted by @
#decorators will take a function as an argument and return a function

#func --> function...
def order(func):#4 func = throw_party
    
    def inner(): #6
        print("Ordering a pizza")#7
        func()#8
    
    return inner   #5  



@order #3
def throw_party():#2
    print("Throwing a party")#9



throw_party()  #1  



