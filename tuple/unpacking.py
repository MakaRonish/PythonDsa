a, b, c = (1, 2, 3)
print(a)
print(b)
print(c)

a, b, c = [5, 6, 7]
print(a)
print(b)
print(c)

# tuple can be create without bracket

z = 1, 2, 3, 4, 5

print(type(z))
y = (1,)
print(type(y))

l = [1, 2, True, True]
print(l.count(2))

a, *b, c = [1, 2, 3, 4, 5, 67]
print(a)
print(b)
print(c)
