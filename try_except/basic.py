
try:
    x=int(input('input a integer'))
    print(x)
    
except:
    print("hello")
else:
    print("ok")
    #if no error it will run this
try:
    x=int(input('input a integer'))
    print(x)
    
except:
    print("hello")
finally:
    print("finally")
    #will print no matter error or not