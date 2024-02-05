def order(func):
    
    def inner(x):
        print('Ordering', x, 'items')
        func(10)
    
    return inner



@order
def throw_party(people):
    print('Throwing a party for', people, 'people!')

throw_party(100)     #inner function
    
    
    

    