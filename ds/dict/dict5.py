sales = {"monday": 100, "tuesday": 200, "wednesday": 300}

print(sales.get("monday"))  # 100

#find heighest sales day
maxSales = sales.get("monday")
day = "monday"
for i,j in sales.items():
    
    if j>maxSales:
        maxSales = j
        day = i

print("Max sales is on ",day," with sales of ",maxSales)        
        
    
    
