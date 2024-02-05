data = [["ram",20],["shyam",30],["malayalam","45"],["hari",40],["gita",50],["sita",60],["rita",25]]

x = sorted(data,key= lambda x : len(x[0]))
print(x)