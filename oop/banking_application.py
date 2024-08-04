class Banking:
    def __init__(self,account_number:int,name:str,account_type:str,branch:str,balance:int=0)->None:
        self.account_number:int=account_number
        self.name:str=name
        self.account_type:str=account_type
        self.branch:str=branch
        self.balance:float=0

    def display(self)->None:
        print(
            f"Account_number={self.account_number}\n"
            f"name={self.name}\n"
            f"account_type={self.account_type}\n"
            f"branch={self.branch}\n"
            f"balance={self.balance}\n"
            )
    
    def balanceChecker(self)->float:
        return self.balance
    
    def deposit(self,amount:float)->None:
        self.balance+=amount
        self.display()

    def withdraw(self,withdraw_amount)->None:
        if self.balance>amount:
            self.balance-=withdraw_amount
            self.display()
        else:
            print("insufficiant balance")
            print(f" available balance:{self.balance}")
    

account_detail:list[Banking]=[
    Banking(12345,"Ronish","Checking","SVP"),
    Banking(12346,"Priya","Saving","chawala"),
    
    ]

while True:
    print("1) Add a account")
    print("2) Display all account")
    print("3) Deposit Money")
    print("4) Withdraw Money")
    print("5) Check balance")
    print("6) Exit")

    choice:int=int(input("option="))
    if choice==1:
        account_number:int=int(input("enter account number="))
        name:str=(input("enter name="))
        account_type:str=(input("enter account_type="))
        branch=(input("enter branch="))
        account_detail.append(Banking(account_number,name,account_type,branch))
    elif choice==2:
        for account in account_detail:
            account.display()
    elif choice==3:
        print("----deposit form----")
        account_number=int(input("account number="))
        for account in account_detail:
            if account.account_number==account_number:
                amount=int(input("amount="))
                account.deposit(amount)
                break
        print("account not found")
        print()
    elif choice==4:
        print("----withdraw form----")
        account_number=int(input("account number="))
        for account in account_detail:
            if account.account_number==account_number:
                amount=int(input("amount to withdraw="))
                account.withdraw(amount)
                break
        print("account not found")
        print()
    elif choice==5:
        account_number=int(input("account number"))
        for account in account_detail:
            if account_number==account.account_number:
                print(f"balance={account.balanceChecker()}")
                print()
                break
    
    elif choice==6:
        withdraw_acc=int(input("Withdraw Account="))
        Deposit_acc=int(input("Deposit Account="))
        amount=int(input("Amount to transfer="))
        validate_withdraw=False
        validate_Deposit=False
        for account in account_detail:
            if account.account_number==withdraw_acc:
                validate_withdraw=True
            elif account.account_number==Deposit_acc:
                validate_Deposit=True
        if not validate_Deposit:
            print("Invalid account to deposit") 
        elif not validate_withdraw:
            print("Invalid account to withdraw")
        elif validate_Deposit and validate_withdraw:
            for account in account_detail:
                if withdraw_acc==account.account_number:
                    account.withdraw(amount)
                elif account.balance>amount:
                    for account in account_detail:
                        if Deposit_acc==account.account_number:
                            account.deposit(amount)
                            break
        
        
                
            

    elif choice==7:
        break

    else:
        print("Invalid")