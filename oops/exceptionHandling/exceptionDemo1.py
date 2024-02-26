

try:
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
    ans = no1 / no2
    #print(ans)
    
except Exception:
    print("Some error occurred")    
except ZeroDivisionError:
    print("Division by zero is not allowed")    
except ValueError:
    print("Please enter valid number")    

else:
    print("No exception occurred")    
    print(ans)


print("End of the program")    