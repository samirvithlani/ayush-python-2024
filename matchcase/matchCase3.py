age = int(input("Enter your age: "))


match age:
    case age if age < 13:
        print("You are a child")
    case age if age >= 13 and age < 18:
        print("You are a teenager")
    case age if age >= 18 and age < 60:
        print("You are an adult")
    case _:
        print("You are a senior citizen")            
        