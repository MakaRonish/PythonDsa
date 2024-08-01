d1 = {"a": 00, "b": 100, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}


def add(d1, d2):
    result = d1.copy()
    for key in d2:
        result[key] = d2[key]
    print(result)
    for keys, value in d1.items():
        samevalue = d2.get(keys, False)
        if samevalue != False:
            result[keys] = result[keys] + value
    print(result)


add(d1, d2)
# aff(d1,d2)
