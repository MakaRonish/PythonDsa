marks = {"a": 1, "b": 2}

marks["b"] = 0
marks["d"] = 4
marks.update({"c": 3})
marks.update(a=0)

print(marks)
# del marks
# print(marks)

print("a" in marks)
