num:float=float(input("Enter a number"))
if num%3==0 and num%5==0:
    print("FOOBAR")
elif num%3==0:
    print("FOO")
elif num%5==0:
    print("Bar")
else:
    print("invalid")