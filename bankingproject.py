def show_balance():
    print(f"Your balance is {balance:.2f}")
    print()

def deposit():
    amount = float(input("Enter an amount to deposit"))
    if amount<0:
        print("That is not a valid amount")
        return 0
        
    else:
        return amount
        

def withdraw():
    amount=float(input("Enter the amount to be withdrawn")) 
    if amount>balance:
        print("Insufficient funds")
        return 0
    elif amount <0: 
        print("Amount must be greater than Zero")
    else:
        return amount
balance=0
running= True
print("BANKING PROGRAM")
print("-----------")
while running:
    
    print("1.Show Balance")
    print("2.Deposit")
    print("3.withdraw")
    print("4.Exit")
    
    choice=input("Enter your choice(1-4)")
    
    if choice =="1":
        show_balance()
    elif choice=="2":
        balance +=deposit()
    elif choice == "3":
        balance =balance-withdraw()
        print(f"Your new amount is {balance:.2f}")
        print()
       
    elif choice == "4":
        running=False
        print("Thank You!!Have a nice day.....")
    else:
        print("That is not a valid input")

