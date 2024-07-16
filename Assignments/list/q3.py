l=[4,8,6,5,3,12,1,7,6,2]

def sumProduct(l)->tuple:
    sum=0
    product=1
    for number in l:
        sum+=number
        product*=number
    
    return sum , product

result=sumProduct(l)
print(f"sum={result[0]}\nproduct={result[-1]}"
      )