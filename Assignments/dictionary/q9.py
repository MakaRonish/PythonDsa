string="ronishMakajuislivingincanada"

def freq(str):
    dic={}
    maxfre=float("-inf")
    maxkey=None
    
    for i in str:
        dic[i]=dic.get(i,0)+1

    for key,value in dic.items():
        if value>maxfre:
            maxfre=value
            maxkey=key
    print(f"THe character with max freq is {maxkey} with {maxfre}")

freq(string)
    