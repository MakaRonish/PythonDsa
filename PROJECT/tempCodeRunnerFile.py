class Business:
    def __init__(self,product_id:int,product_name:str,price:float)->None:
        self.product_id=product_id
        self.product_name=product_name
        self.price=price

    def updatePrice(self,new_price:float)->None:
        if new_price!=0:
            self.price=new_price
        else:
            print("price cannnot be 0")

    def updateName(self,new_name)->None:
        if new_name!="":
            self.product_name=new_name
        else:
            print("name cannot be empty")
    
    def displayProduct(self)->None:
        print(f"product Id={self.product_id}")
        print(f"product name={self.product_name}")
        print(f"product price={self.price}")
        print()

product_detail=[
    Business(1,"shoe",200),
    Business(2,"grocery",100),
    Business(3,"cloth",150),
    Business(4,"accesorry",50),
    Business(5,"instrument",500),
    
    ]
print(product_detail[1].price)