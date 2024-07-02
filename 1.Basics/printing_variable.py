name = "Ronish"
age = 18
gender = "Male"

print("My name is", name)  # , will put space automaticly
print("my anem is",name,"my age is",age)

# method-2 f string
print(f"My name is {name}")

#method 3(identfiers)
"""
%s->String
%d->Integer
%f->Float
"""

print("My name is %s, age %d gender%s"%(name,age,gender))

#methond 4 for debug
print(f"{name=}")
"""to check what is store in variable"""