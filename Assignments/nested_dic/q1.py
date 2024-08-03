detail: dict = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [56, 78, 56, 12, 33, 56],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
    # "Anirudh": [1,2],
    # "Sanjay": [1,2],
    # "Muskan": [1],
    # "Nihar": [1],
    # "Akshay": [1],
}


def printRead(dic: dict) -> None:
    # for name in dic:
    #     print(name, end=": ")
    #     lenght = len(dic[name])
    #     c = 0
    #     for marks in dic[name]:
    #         c += 1
    #         if lenght == c:
    #             print(marks, end="")
    #         else:
    #             print(marks, end=", ")
    #     print()
    for name in dic:
        print(f"{name}:{",".join(str(m) for m in dic[name])}")


# printRead(detail)
# l=[1,2,3,4,5]
# print("_".join( str(a) for a in l))

def highestMark(dic: dict) -> None:
    for name in dic:
        max = 0
        for marks in dic[name]:
            if marks > max:
                max = marks
        print(f"{name}:{max}")


# highestMark(detail)


def highestallMark(dic: dict) -> None:
    highestMark = 0
    same_highest_mark = {}
    print(len(same_highest_mark))
    for name in dic:
        max = 0
        for marks in dic[name]:
            if marks > max:
                max = marks
        if max > highestMark:
            highestMark = max
            highest_scorer = name
    for name in dic:
        if highestMark in dic[name]:
            same_highest_mark[name] = highestMark

    print(f"THe highest mark is {highestMark},", end="scored by")
    for name in same_highest_mark:
        print(f",{name}", end="")


# highestallMark(detail)

def average(dic:dict)->None:
    for name in dic:
        total=0
        
        for marks in dic[name]:
            total+=marks
        print(f"{name}:{(total/len(dic[name])):.2f}")
# average(detail)
def HighestAverage(dic:dict)->None:
    highest_avg=0
    person=""
    avgall={}
    for name in dic:
        total=0
        for marks in dic[name]:
            total+=marks
        avg=total/len(dic[name])
        avgall[name]=avg
        if avg>highest_avg:
            highest_avg=avg
    print(f"The highest average mark is {highest_avg} by",end=" ")
    for name in avgall:
        if avgall[name]==highest_avg:
            print(name,end=" ")
            
# HighestAverage(detail)

def totalSub(dic:dict)->None:
    for name in dic:
        sub=0
        for subjects in dic[name]:
            sub+=1
        print(f"{name}:{sub}")
# totalSub(detail)

def more(dic:dict,num:int)->None:
    print(f"Student who scored more than {num}")
    for name in dic:
        l=[]
        for marks in dic[name]:
            if num<marks:
                l.append(marks)
        if len(l)!=0:
            print(f"{name}:{l}")
more(detail,75)





