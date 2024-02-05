user= {"name":"ram","role":"manager1"}
def accessData(func): #func = getData
    
    def inner():
        if user["role"]=="manager":
            print("Accessing data")
            func()
        else:
            print("You are not allowed to access data")

    return inner

@accessData
def getData():
    print("Getting data")                



getData()    