def loginRequired(func):
    
    def inner(**kwargs):
        print("kwargs....",kwargs)
        if kwargs["role"] == "admin":
            print("Welcome  admin ")
            func({"name":kwargs["name"],"role":kwargs["role"]})
        else:
            print("you are not admin..")
            
    return inner           


@loginRequired
def home(user):
    print("Home page....",user)


home(name="ram",role = "admin")    


