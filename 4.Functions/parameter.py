def average(num1:int,num2:int,num3:int):

    avg=int((num1+num2+num3)/3)
    print(avg)

average(1,2,3)


def marks(subject1,subject2,subject3,subject4,subject5):
    total=subject1+subject2+subject3+subject4+subject5
    percentage=total/500*100
    print(f"Total={total}\nPercentage={percentage}")
marks(90,50,80,30,70)