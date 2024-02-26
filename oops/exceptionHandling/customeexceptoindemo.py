class InvalidAgeException(Exception):
    
    def __init__(self,message) :
        super().__init__(message)
        




try:
    age = int(input("Enter your age: "))        
    if age<18:
        raise InvalidAgeException("You are not eligible to vote")
except InvalidAgeException as e:
    print(e)    
        