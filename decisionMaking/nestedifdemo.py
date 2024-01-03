age = 15

if age>=18:
    print("You are eligible to vote!!")
    
    if age>=21:
        print("You are eligible to drive!!")
        
        if age>=60:
            print("You are eligible to retire!!")
        else:
            print("You are not eligible to retire!!")    
            
    else:
        print("You are not eligible to drive!!")    


else:
    print("You are not eligible to vote!!")
    if age>=16:
        print("You are eligible to ride activa!")        
    else:
        print("You are not eligible to ride activa!")
            