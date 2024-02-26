from multipledispatch import dispatch


class Amazone:
    
    @dispatch(str)
    def search(self, pname):
        print("Searching for", pname)
    
    @dispatch(str, str)
    def search(self, pname, category):
        print("Searching for", pname, "in", category)
    
    @dispatch(str, int)
    def search(self,pname,pprice):
        print("Searching for", pname, "in", pprice)    



a = Amazone()
#a.search("Mobile")
#a.search("Mobile", "Electronics")
a.search("Mobile", 10000)
        
        