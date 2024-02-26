class Google:
    country = "USA"
    g = "Google"
    def __init__(self):
        print("Google class constructor")
        self.name = "Google"
        self.fund = 100
        self.ceo = "Sundar Pichai"


class Alphabet:
    country = "japan"
    a = "Alphabet"
    def __init__(self):
        print("Alphabet class constructor")
        self.name = "Alphabet"
        self.fund = 200
        self.president = "Larry Page"



class Youtube(Alphabet,Google):
    def __init__(self):
        super().__init__()
        print("Youtube class constructor")
    
    def getCompanyData(self):
        print("Name: ",self.name)
        print("Fund: ",self.fund) 
        #print("CEO: ",self.ceo)
        #print("President: ",self.president)
        print("Country: ",self.country)
        print("Google: ",self.g)
        print("Alphabet: ",self.a)
                       
        

y = Youtube()
y.getCompanyData()        