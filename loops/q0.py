def ask():
    count=0
    while True:
        a=int(input("number:"))
        
        if a==0:
            break
        count+=1
    print("number of attempt you take:",count)

ask()