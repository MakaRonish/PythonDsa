class Rectangle:
    def __init__(self, lenght:float=0, breath:float=0)->None:
        self.length = lenght
        self.breath = breath
    
    def __str__(self)->str:
        return (f"length:{self.length}\nbreath:{self.breath}")

    def area(self)->float:
        return self.length * self.breath

    def perimeter(self)->float:
        return 2 * (self.length + self.breath)

    def square(self)->bool:
        # if self.length == self.breath:
        #     return True
        # return False
        return self.length==self.breath


o1 = Rectangle(20, 20)
print(o1)
print(o1.length)
print(o1.area())
print(o1.perimeter())
print(o1.square())
