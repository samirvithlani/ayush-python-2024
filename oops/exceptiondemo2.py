try:
    no1 = int(input("Enter first number: "))
    print("no1 = ", no1)
except ValueError as e:
    print(e)    