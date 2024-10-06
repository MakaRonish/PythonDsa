# not proper way
# f = open(
#     "text.txt",
#     "r",
# )

# print(f.name)
# f.close()


# context manager we dont need to close file now

with open("text.txt", "r") as f:
    f_content = f.readline()
    print(f_content)

print(f_content)

# one line at a time
with open("text.txt", "r") as f:
    for line in f:
        print(line, end="")

with open("text.txt", "r") as f:
    for line in range(11):
        a = f.readline()
        print(a, end="")

with open("text.txt", "r") as f:
    f_content = f.read(10)
    print(f_content)

with open("text.txt", "r") as f:
    f_content = f.readlines()
    print(f_content)
    for i in range(len(f_content)):
        f_content[i] = f_content[i].strip("\n")
    print(f_content)

with open("text.txt", "r") as f:
    size = 50
    f_content = f.read(size)

    while len(f_content) > 0:
        print(f_content, end="")
        f_content = f.read(size)

# tell will tell the position
with open("text.txt") as f:
    f_content = f.read(20)
    print(f.tell())

# to reset the cursor/ put at a position .seek(n)

with open("text.txt") as f:
    f_content = f.read(20)
    print(f_content)
    print(())
    f.seek(10)
    f_content = f.read(20)
    print(f_content)


# writing

with open("text2.txt", "a") as f:
    f.write("\ntest3")


with open("text.txt", "r") as rf:
    with open("textcopy.txt", "w") as wf:
        for i in rf:
            wf.write(i)

# binay mode for image

with open("prac.JPG", "rb") as rf:
    with open("textcopy.JPG", "wb") as wf:
        pic = rf.read(10)
        wf.write(pic)
