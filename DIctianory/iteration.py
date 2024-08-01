marks={ 
    "history":90,
    "chem":80,
    "sci":70,
    "phy":60,
    "math":50,
    "eng":40,
}
# total=0
# for i in marks:
#     total+=marks[i]
#     print(marks[i])
# print(total)

max=0
subject=""
for i in marks:
    mark=marks[i]
    if mark>max:
        max=mark
        subject=i

print(max)
print(subject)