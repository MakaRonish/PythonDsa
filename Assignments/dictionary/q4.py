def keyCHecker(dic: dict, key: str) -> bool:
    a = dic.get(key, False)
    if a != False:
        return True

    return False


dic = {"1": "a"}
print("1" in dic)
print(keyCHecker(dic, "0"))
