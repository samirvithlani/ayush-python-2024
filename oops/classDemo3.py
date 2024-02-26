class Vehlicle:
    
    def __init__(self,name,price):
        self.name = name #instance variable
        self.price = price
    
    def getVehlicleDetail(self):
        print("Vehlicle Name: ",self.name)
        print("Vehlicle Price: ",self.price)    
        
        


v = Vehlicle("BMW",1000000)        
v.getVehlicleDetail()