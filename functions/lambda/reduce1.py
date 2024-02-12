from functools import reduce

#map -->it will return array of values with same length
#filter --> it will return array of values with less length or same length
#reduce --> it will return single value


marks = [10,20,30,40,50]
#10,20 --> 30
#30,30 --> 60
#60,40 --> 100
#100,50 --> 150
total = reduce(lambda a,b:a+b,marks)
print(total)

address = ["a -304","abc street","bangalore","karnataka"]

add = reduce(lambda a,b:a+" "+b,address)
print(add)


