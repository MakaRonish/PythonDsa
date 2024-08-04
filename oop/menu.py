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
    
    def updateDetail(self,new_name=None,new_age=0,new_gender=None):
        if new_name:
            self.name=new_name
        elif new_age:
            self.name=new_age
        elif new_gender:
            self.name=new_gender

    def total(self):
        tot = 0
        for m in self.mark:
            tot += m
        return tot


student_data:list[Student] = [
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
        "Display all student (4)\n"
        "Display a student (5)\n"
        "Exit (5)\n"
        )
    choice=int(input("option:"))
    if choice==1:
        Roll_no=int(input("roll no="))
        name=(input("name="))
        age=int(input("age="))
        gender=(input("roll no="))
        student_data.append(Student(Roll_no,name,age,gender))
    elif choice==2:
        name=input("name of student you wanna remove")
        remove_student_index=0
        for i in student_data:
            if name ==i.name:
                remove_student_index=student_data.index(i)
                deleted_std=student_data.pop(remove_student_index)
                break
        
        deleted_std=student_data.pop(remove_student_index)  
        for students in student_data:
            students.display()

    elif choice==3:
        roll=int(input("roll of student you wanna update value of"))
        new_name=input("enter new name")
        age=int(input("enter new age"))
        gender=(input("enter new gender"))
        for object in student_data:
            if object.Roll_no==int(roll):
                object.updateDetail(new_name,age,gender)
        
                
    elif choice==4:
        if len(student_data)==0:
            print("no students")
        else:
            for students in student_data:
                students.display()
    elif choice==5:
        name1=input("enter the name of student:")
        for object in student_data:
            if object.name==name1:
                object.display()
    elif choice==6:
        break
    else:
        print("invalid")