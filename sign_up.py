class Login:
    def __init__(self,name,password):
        self.name=name
        self.password=password


 
accounts=[Login("ronish","ronish123"),Login("priya","hello")]

def main_login():
    while True:
        print("1)Create new Account\n2)Log in to existing account\n3)Exit")
        try:
            option=int(input("option="))
        except ValueError:
            print("pls enter a number")
        if option==1:
            name=input("Username=")
            password=input("password=")
            accounts_exist=False
            for i in range(len(accounts)):
                if accounts[i].name==name:
                    print("Username already exist")
                    accounts_exist=True
                    break
            if not accounts_exist:
                new_user=Login(name,password)
                accounts.append(new_user)
                print("accound created sucessfully")
            
        elif option==2:
            name=input("Username=")
            password=input("password=")
            accounts_exist=False
            for i in range(len(accounts)):
                if accounts[i].name==name and accounts[i].password==password:
                    print(f"Log in as {accounts[i].name}")
                    accounts_exist=True
                    break
            if not accounts_exist:
                print("either your password or username is worng")
            else:
                break
        elif option==3:
            break
main_login()
        


        




