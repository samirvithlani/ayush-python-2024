#**kwargs

def getUserData(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
    

getUserData(name="John",age=30,city="Delhi",state="Delhi",x=100)    