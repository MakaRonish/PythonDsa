detail={
    "a":[20,30,40,50,60],
    "b":[20,40,40,50,60],
    "c":[20,50,40,50,60],
    "d":[20,60,40,500],
    "e":[20,70,40,50,60],

}
a="0"
for i in a:
    print(i)

def displayTotal(dic:dict):
    max=0
    person=""
    for key in dic:
        total=0
        # for marks in dic[key]:
        #     total+=marks
            # print(f"{key} has scored {total} marks")
        for marks in range(0,len(dic[key])):
            total+=dic[key][marks]
            
        print(f"{key} has scored {total} marks")
        if total>max:
            max=total
            person=key
        
        print(f"{person} has the highest marks {max}")
displayTotal(detail)

