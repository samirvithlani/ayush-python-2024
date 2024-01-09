no = int(input("Enter a number: "))
count = 0
#123 > 0 True
#12 > 0 True
#1 > 0 True
#0 > 0 False
while no>0:
    #count = 1
    #count = 2
    #count = 3
    count+=1
    #123 = 123//10 = 12
    #12 = 12//10 = 1
    #1 = 1//10 = 0
    no = no // 10

print("Total digits: ",count)    