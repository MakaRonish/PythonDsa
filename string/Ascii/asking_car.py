def loopasking():
    word=""
    while True:
        cha=input("Enter char = ")
        if cha=="q" or cha=="Q":
            break
        word+=cha
    print(word)
loopasking()