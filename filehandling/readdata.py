# file = open("./demo.txt", "r")
# data = file.read() # Read the entire file
# print(data)



file = open("./demo.txt", "r")
cnt = 0
for i in file:
    cnt += 1
    print(i,end="") # Read the entire file line by line

print("Total lines in the file are: ", cnt)    