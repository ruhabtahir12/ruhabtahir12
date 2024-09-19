
accounts={}
 
is_passowrd=True
while True:
    print("Welcome to account management system!")
    print()
    print("1. Create an account")
    print("2. Update an account")
    print("3. Delete an account")
    print("4. View account")
    print("5. Quit")
    choice=int(input("Enter your choice between 1-6 options:"))

    
        
    if choice==1:
        account_no=int(input("Enter the account number of employee to add:"))
        income=int(input("Enter the income of employee:"))
        accounts[account_no]=income
        print(accounts)
    elif choice==2:
        account_no=int(input("Enter the account no to update"))
        income=int(input("Enter the amount to update:"))
        password=input("Enter the passowrd:")
        if is_passowrd==True:
            if account_no in accounts:
            
                accounts[account_no]=income
            else:
                print(f"{account_no} has not been working in company")
        print(accounts)
    elif choice==3:
       
        account_no=int(input("Enter the account to delete:"))
        if account_no in accounts:
            del accounts[account_no]
        else:
            print(f"{account_no} not found")
        print(accounts)
    elif choice==4:
            for key,value in accounts.items():
                print(f"{key}:{value}")
    elif choice==5:
        print("Quit")
        break
    else:
        print("Please enter the right choice number from menu")


        
    