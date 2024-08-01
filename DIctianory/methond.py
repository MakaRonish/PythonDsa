marks = {
    "history": "90",
    "chem": 80,
    "sci": 70,
    "phy": 60,
    "math": 50,
    "eng": 40,
}

# marks.clear()
print(marks.get("history", "doesnt exist"))
print(marks)


def gettt(d:dict,k:str,text:str):
    keys=[]
    for i in d:
        keys.append(i)
    if k not in keys:
        print(text)
gettt(marks,"h","0")


a=marks.pop("eng")
print(a)

marks.update(s=99,k=900)
print(marks)
    
    