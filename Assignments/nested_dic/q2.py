detail={
    "Anirudh":{
        "age":56,
        "gender":"Male",
        "marks":[1],
        "adult":True,
    },
    "Muskan":{
        "age":16,
        "gender":"female",
        "marks":[2],
        "adult":False,
    },
    "Nihar":{
        "age":24,
        "gender":"male",
        "marks":[0],
        "adult":True,
    },
}

def age(dic:dict,num:int)->None:
    for name in dic:
        if dic[name]["age"]>num:
            print(f"{name}:{dic[name]["age"]}")
# age(detail,17)

def adult(dic:dict)->None:
    for name in dic:
        if dic[name]["adult"]:
            print(name)
# adult(detail)

def avg(dic:dict)->None:
    for name in dic:
        total=0
        for mark in dic[name]["marks"]:
            total+=mark
            avg=total/len(dic[name]["marks"])
        print(f"{name}:{avg:.2f}")
# avg(detail)

def highest_mark(dic:dict)->None:
    for name in dic:
        max=0
        for mark in dic[name]["marks"]:
            if mark>max:
                max=mark
        print(f"{name}:{max}")
# highest_mark(detail)
def subject(dic:dict)->None:
    for name in dic:
        if len(dic[name]["marks"])>3:
            print(name)
# subject(detail)

def total(dic:dict):
    for name in dic:
        total=0
        for mark in dic[name]["marks"]:
            total+=mark
        print(f"{name}:{total}")
# total(detail)

def youngest(dic:dict)->None:
    low_age=float("inf")
    person=""
    for name in dic:
       if dic[name]["age"]<low_age:
           low_age=dic[name]["age"]
           person=name
    print(f"The youngest student is {person}, age {low_age}")
# youngest(detail)

def highavg(dic:dict):
    highest=0
    hi={}
    for name in dic:
        total=0
        for mark in dic[name]["marks"]:
            total+=mark
            avg=total/len(dic[name]["marks"])
        if avg>highest:
            highest=avg
            hi[name]=avg
    print(f"The student with highest avg{highest} is",end=" ")
    for name in hi:
        if hi[name]==highest:
            print(name,end=" ")
highavg(detail)

    
    

    

