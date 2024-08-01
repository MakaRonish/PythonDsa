detail={
    "Ronish":{
        "age":18,
        "gender":"male",
        "marks":[10,20],
        "adult":True
    },
    "priya":{
        "age":19,
        "gender":"female",
        "marks":[10,20,30],
        "adult": True
    },
    "makaju":{
        "age":40,
        "gender":"none",
        "marks":[10,20,40,50],
        "adult":False
    },
}

print(detail["priya"]["gender"])
print(detail["priya"]["marks"][-1])

for key in detail:
    if detail[key]["adult"]:
        print(f"{key} is adult and her age is {detail[key]["age"]}")

def marks(dic:dict):
    for key in dic:
        total=0
        for mark in dic[key]["marks"]:
            if mark > total:
                total=mark
        print(f"{key} has highest {total} marks")

marks(detail)