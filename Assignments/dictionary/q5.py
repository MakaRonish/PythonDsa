dic={"1":"a","3":"d"}
dic1={"1":"b","2":"c"}

dic={'apple':3,"banana":5,"cherry":7}
dic1={'apple':9,"orange":10,"banana":8}

# dic.update(dic1)
# print(dic)

for i, j in dic1.items():
    dic[i]=j
print(dic)
