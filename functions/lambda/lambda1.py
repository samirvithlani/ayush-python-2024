#anno functions..


fun1 = lambda : print("Hello World")
fun1()

fun2 = lambda x: print("x = ",x)
fun2(100)

fun3 = lambda name,surname: print("Hello",name+" "+surname)
fun3("Raj","Kumar")

fun4  = lambda x ,y : x+y
print("Sum = ",fun4(10,20))



fun5 = lambda x ,y : x if x >y else y
print("Max = ",fun5(10,20))

func6 = lambda x,y,z : x if x >y and x >z else y if y >z else z
print("Max = ",func6(10,20,30))


