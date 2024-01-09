#123 1 + 2 + 3 = 6
no =123
rem = 0
sum = 0
#12>0 True
while no>0:
    
    rem = no % 10 #123 % 10 = rem = 3, 12 % 10 = rem = 2, 1 % 10 = rem = 1
    sum = sum + rem #sum = 0 + 3 = 3, 3 = 3 + 2 = 5,5 = 5 + 1 = 6
    no = no // 10 #123 // 10 = no = 12,12//10 = no= 1,0


print("Sum of digits: ",sum)    
    
