#map -will  return a list of same length as the input list


data = ["jay","ram","shyam","hari","gita","sita","rita"]


x = list(map(lambda x:x.upper(), data))
print(x)

# test = lambda x:x.upper()

# test("amit")


data = [[10,20],[40,50],[50,70],[90,100]]

ans = list(map(lambda x:list(map(lambda y:y+10,x)),data))
print(ans)


names = [["ram","sharma"],["neha","dhupiya"],["amit","kumar"]]
fullNames = list(map(lambda x: x[0]+" "+x[1],names))
print(fullNames)




