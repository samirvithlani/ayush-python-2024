
#mutable : we can change with same reference
#immutable : we can not change with same reference
#string is immutable
#in python string declaration with ""
#in python string declaration with ''
#string stores data in array form
#string is a collection of characters
#string is iterable
#subscritable : we can access the data with index

name = "Ram seeta"
print(name)
print(name[0])

l = len(name)
print("Length of string is ",l)

# for i in range(0,l):
#     print(name[i])


# for i in range(0,len(name)):
#     print(name[i],end="")

for i in name:
    print(i,end="")