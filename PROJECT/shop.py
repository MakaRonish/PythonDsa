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

    
def checkout():
    products={}
    def total(products)->float:
        t=0
        for values in products.values():
            t+=values
        return t

    while True:
        print("1) Add product")
        print("2) Remove product")
        print("3) checkout")
        print("4) item list")

        choice=int(input("Enter the option:"))
        if choice==1:
            i=1
            for product in product_detail:
                print(i)
                i+=1
                product.displayProduct()
            item=int(input("which item do you want to add"))
            products[product_detail[item-1].product_name]=products.get(product_detail[item-1].price,0)+product_detail[item-1].price
            print(products)
            print(total(products))
        elif choice==2:
            print(products)
            item=input("which item do you want to remove=")
            if item in products:
                products.pop(item)
                print(products)
            else:
                print("wrong product")
        elif choice==3:
            print(products)
            print(total(products))
            break
        elif choice==4:
            for product in product_detail:
                product.displayProduct()
        else:
            print("invalid option")

checkout()
        
        


            


            
