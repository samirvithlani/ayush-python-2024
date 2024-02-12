def smartdiv(func):
    def inner(a,b):
        if b ==0:
            print("Division by zero is not allowed")
            return
        else:
            func(a,b)
    
    return inner


@smartdiv
def div(a,b):
    print(a/b)        

div(10,2)    