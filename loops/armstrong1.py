#153 --> 1634 -> .....

no = int(input("Enter a number: "))
tempNO = no
noOfDigits = 0
while tempNO>0:
    tempNO = tempNO//10
    noOfDigits += 1

temp2 = no
rem = 0
sum =0
while temp2 >0:
    rem = temp2%10
    sum = sum + rem **noOfDigits
    temp2 = temp2//10


if sum == no:
    print("Armstrong")
else:
    print("Not Armstrong")        
    
  
    
