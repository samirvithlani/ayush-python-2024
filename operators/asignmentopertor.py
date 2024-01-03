# = is assignment operator, right side value is assigned to left side variable
x = 10
y = 5

x = x + y # x = 15
y = x - y # y = 15 - 5 = 10
x = x - y # x = 15 - 10 = 5


# x = (x+y) - x
# y = (x+y) + y
print("x is", x)
print("y is", y)

p = 10
q = 5

p = p *q # p = 50
q = p // q # 50 // 5 = 10
p = p // q # 50 // 10 = 5

print("p is", p)
print("q is", q)