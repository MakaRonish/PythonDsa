class StudentDetail:
    #class variable/attribute
    # id=0
    # name=""
    # age=0
    # gender=""

    #magic
    def __init__(self,id,age,gender,name):
        self.id=id
        self.gender=gender
        self.age=age
        self.name=name
        
        
    
    #methods
    # def setDetail(self):
    #     self.id=int(input("id"))
    #     self.gender=input("gender")
    #     self.age=int(input("age"))
    #     self.name=input("name")
    #     self.address="naruto"

    def display(self):
        print(f"ID = {self.id}")
        print(f"gender = {self.gender}")
        print(f"age = {self.age}")
        print(f"name = {self.name}")
    
    def updateName(self,new_name:str):
	    self.name=new_name

        

s1=StudentDetail(1,18,"male","ronish")





