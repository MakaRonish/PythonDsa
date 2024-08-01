marks = {
    "history": 90,
    "chem": 80,
    "sci": 70,
    "phy": 60,
    "math": 50,
    "eng": 40,
}

print(marks.keys())
print(marks.values())
print(marks.items())
l = list(marks.items())
print(l[0])

for i,k in l: #unpacking
    print(i,k)
