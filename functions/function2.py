def getPalindromeList(data):
    
    return [x for x in data if x == x[::-1]]


print(getPalindromeList(["abc","aba","xyz","1221","12321","12345"]))
            