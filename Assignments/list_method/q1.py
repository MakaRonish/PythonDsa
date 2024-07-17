def list_reverse():
    l = []
    result = []
    for i in range(10):
        element = int(input(f"Enter element{i+1}:"))
        l.append(element)
    for index in range(len(l) - 1, -1, -1):
        result.append(l[index])
    print(result)


list_reverse()
