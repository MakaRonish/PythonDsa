"""
Continu(skips the below part of loop)
break (break the loop)
"""

i=1
while i<=10:
    print("hello")
    i+=1
    if i==2:
        continue
    if i==9:
        break
    print("bye")