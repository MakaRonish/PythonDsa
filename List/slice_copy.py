a = [1, 2, 3, 4, 6, 7, [3, 4]]
print(id(a))
# c = a
b = a[:]
print(id(b))
print("b")

# a = [1, 23]
# print(id(a))
# a[:] = [1, 23]
# print(id(a))

b[0] = 10


print(a)
print(b)
