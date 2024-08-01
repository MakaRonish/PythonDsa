total_student=int(input("number of student="))
def marks(total_students:int)->dict:
    mark={}
    for i in range(total_students):
        sub=input("Enter the subject Name=")
        mar=int(input("Enter the subject Name="))
        mark[sub]=mar
    return mark

print(marks(total_student))

