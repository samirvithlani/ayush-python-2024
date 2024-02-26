class Test:
    #instance variable
    #static variable
    #local variable
    
    a = 10 #static variable
    
    def getData(self):
        #self --> current object
        x = 20 #local variable
        self.y = 30 #instance variable
        print("I am a method")
        
    def printData(self):
        print("I am a method")
        print(self.y)    



t = Test()
t1 = Test()
t.getData() #error....
t1.printData()
#it will pass class's current object as an argument to the method
        
    
    