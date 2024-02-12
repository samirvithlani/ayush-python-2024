age = 20
file = open("./filehandling/demo3.txt","a")
print("Hello this line is written by file handling",file=file)
print("age = ",age,file=file)
file.close()
