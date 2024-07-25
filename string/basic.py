a="ronish"
for i in a:
    print(i)

print(len(a))

for i in range(-1,-len(a)-1,-1):
    print(a[i],end="")


for ch in a[::-1]:
    print(ch)