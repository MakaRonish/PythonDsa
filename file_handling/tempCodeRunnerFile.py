with open("prac.JPG", "rb") as rf:
    with open("textcopy.JPG", "wb") as wf:
        pic = rf.read(10)
        wf.write(pic)