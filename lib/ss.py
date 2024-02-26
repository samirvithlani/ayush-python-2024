import pyscreenshot
import time
count=0
while True:
    count+=1
    absolute_path = "D://demo"+str(count)+".png"
    print("screen shot taken")
    print(absolute_path)
    image = pyscreenshot.grab()
    image.save(absolute_path)
    time.sleep(10)
    
