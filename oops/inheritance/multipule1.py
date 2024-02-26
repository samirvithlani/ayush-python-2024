#1 paren n child....

class Gov:
    def __init__(self):
        print("Gov class constructor")
        self.party = "BJP"
        self.country = "India"
        self.pm = "Modi"


class State(Gov):
    def __init__(self):
        super().__init__()
        print("State class constructor")
    def getGovData(self):
        print("Party: ",self.party)
        print("Country: ",self.country)
        print("PM: ",self.pm) 


class City(Gov):
    
    def __init__(self):
        super().__init__()
        print("City class constructor")
    
    
    def getGovData(self):
       print("Party: ",self.party)
       print("Country: ",self.country)
       print("PM: ",self.pm)                    
        


c = City()
c.getGovData()

s = State()
s.getGovData()        