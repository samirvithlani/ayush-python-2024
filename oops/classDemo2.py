#constructor : constructor is special method in python which is used to initialize the instance of class.


class Bank:
    
    def __init__(self):
        print("I am a constructor")
        self.balance = 0
        self.name = "SBI"
    
    
    def getBankDetail(self):
        print("Bank Name: ",self.name)
        print("Bank Balance: ",self.balance)
        


b = Bank() #constructor will be called
b.getBankDetail()        
            