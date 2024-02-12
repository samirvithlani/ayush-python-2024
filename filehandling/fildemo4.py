def writeData():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    salary = float(input("Enter your salary: "))
    
    data = {"name":name,"age":age,"salary":salary}
    file = open("./filehandling/demo4.txt","a")
    file.write(str(data))
    file.close()

writeData()    
