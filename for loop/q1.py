start=int(input("Enter a number:"))
end=int(input("Enter a number:"))
sum=0
seven=0
for i in range(start,end+1):
    print(i,end=" ")
    sum+=i
for i in range(start,end+1):
    print(i,end=" ")
    if i%7==0:
        seven+=i

print("total is ",sum)
print("total is seven",seven)

