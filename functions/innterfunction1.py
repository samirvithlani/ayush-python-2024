def outer():
    print('Outer function')
    def inner():
        print('Inner function')
        
    inner()

outer()
# inner()  # NameError: name 'inner' is not defined        