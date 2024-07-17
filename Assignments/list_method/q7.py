l=[10,20,30,4]
def sum_avg(l:list):
    sum=0
    
    for i in l:
        sum+=i
    avg=sum/len(l)
    print(f"sum={sum}\navg={avg}")

sum_avg(l)

    