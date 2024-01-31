
def sort_by(products,key):
    for  p in products:
        for i,j in p.items():
            for k,l in j.items():
                print(k,l)
                    
    


products = [{"iphone":{"price":1000,"ratings":4}},{"iphone":{"price":1000,"ratings":4}}]
sort_by(products,"price")    
    







