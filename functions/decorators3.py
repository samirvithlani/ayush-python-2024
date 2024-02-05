
def eligible(func): #application
    
    def inner():
        print("Checking eligibility")
        func() #application()
    
    return inner




@eligible
def application():
    print('application')

application()    