
import Myexception
name = "ram"



try:
    if " " in name:
        raise Myexception.InvalidString("String contains space")

except Myexception.InvalidString as e:
    print(e)

else:
    print("No exception occurred")        