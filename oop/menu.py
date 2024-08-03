class Student:
    def __init__(self, Roll_no, name, age, gender, mark=[]):
        self.Roll_no = Roll_no
        self.name = name
        self.age = age
        self.gender = gender
        self.mark = mark

    def display(self):
        print(f"roll:{self.Roll_no}")
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"gender:{self.gender}")
        print(f"marks:{self.mark}")

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


while True:
    print(
        "Add a student (1)\n"
        "Remove a student (2)\n"
        "update a student (3)\n"
        "Display a student (4)\n"
        "Exit (5)\n"
        )
    choice=int(input("option:"))
    if choice==1:
        Roll_no=int(input("roll no="))
        name=(input("roll no="))
        age=int(input("roll no="))
        gender=(input("roll no="))
        student_data.append(Student(Roll_no,name,age,gender))
    elif choice==2:
        name=input("name of student you wanna remove")
        remove_student_index=0
        for i in student_data:
            if name ==i.name:
                deleted_std=student_data.pop(remove_student_index)
                remove_student_index=student_data.index(i)
        deleted_std=student_data.pop(remove_student_index)  
        for students in student_data:
            students.display()

    elif choice==3:
        name=input("name of student you wanna update value of")
        stuff=input("what to update:")
        student_index=0
        for i in student_data:
            if name ==i.name:
                if stuff=="Roll_no":
                    i.Roll_no=int(input("New Roll:"))
                elif stuff=="gender":
                    i.gender=(input("New Roll:"))
                elif stuff=="age":
                    i.age=int(input("New Roll:"))
                elif name=="name":
                    i.name=(input("New Roll:"))
                
    elif choice==4:
        if len(student_data)==0:
            print("no students")
        else:
            for students in student_data:
                students.display()
    elif choice==5:
        break
    else:
        print("invalid")