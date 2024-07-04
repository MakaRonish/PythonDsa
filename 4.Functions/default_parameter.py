def marks(subject1, subject2=0, subject3=0, subject4=0, subject5=0):
    total = subject1 + subject2 + subject3 + subject4 + subject5
    percentage = total / 500 * 100
    print(f"Total={total}\nPercentage={percentage}")


marks(80, 30, 70)
