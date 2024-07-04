def marks(subject1:int,subject2:int,subject3:int,subject4:int,subject5:int)->bool:
    percentage=(subject1+subject2+subject3+subject4+subject5)/5
    print(percentage>33)
    if percentage>33:
        return percentage>33
    else:
        return percentage>33

    #better way
    """
    return percentage>33

    or 

    if percentage<33:
        return false
    return True
    """
    

print(marks(10,10,10,10,10))
    