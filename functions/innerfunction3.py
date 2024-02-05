def checkName(name):
    
    def isSpace(name):
        if ' ' in name:
            return True
        
    def isSatringWith(name):
        if name.startswith('Mr.') or name.startswith('Mrs.'):
            return True
    
    
    return isSpace(name) and isSatringWith(name)    


ans = checkName('Mr.John')  # True
print(ans)
            