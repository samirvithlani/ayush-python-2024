#overriding ....parent class same method develope in child class with same signature called overriding
#signature inncludes method name and parameter list

class Area:
    
    def findArea(self,data):
        print("Area of square is", data*data)


class Square(Area):
    
    
    def findArea(self, data):
        print("Area of square is", data*data)
        super().findArea(5)
    


s = Square()
s.findArea(5) #Area of square is 25                