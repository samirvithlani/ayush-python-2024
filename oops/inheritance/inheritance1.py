#inheritance is process that child class can use properties of parent class
#extends 
class Vehicle:
    
    def __init__(self):
        print("Vehicle class constructor")
        self.seats = 0
        self.wheels = 0


class Car(Vehicle):
    
    def __init__(self):
        super().__init__()
        print("Car class constructor")
    
    def getCarData(self):
        self.seats = input("Enter number of seats: ")
        self.wheels = input("Enter number of wheels: ")
    
    def printCarData(self):
        print("Seats: ",self.seats)
        print("Wheels: ",self.wheels)    
        
    

c = Car() #Car class constructor
c.getCarData()
c.printCarData()