class Student:
    def __init__(self, Roll_no, name, age, gender, mark=[]):
        self.Roll_no = Roll_no
        self.name = name
        self.age = age
        self.gender = gender
        self.mark = mark

    def display(self):
        print(self.Roll_no)
        print(self.name)
        print(self.age)
        print(self.gender)
        print(self.mark)

    def total(self):
        tot = 0
        for m in self.mark:
            tot += m
        return tot


student_data = [
    Student(1, "ronish", 19, "male"),
    Student(2, "priya", 20, "female", [90, 100, 89]),
]

print(student_data[1].age)
print(student_data[1].total())
