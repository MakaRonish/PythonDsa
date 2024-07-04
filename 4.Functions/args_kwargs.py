#*args it will be tuple 
def show(n1,n2,*n3):
    print(f"n1={n1}")
    print(f"n2={n2}")
    print(f"n3={n3}")
    
show(10,20,30,40,50)