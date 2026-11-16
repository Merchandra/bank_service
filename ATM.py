#-------------ATM---------------------

Account_no    = 2005
Customer_name = "Priya"
Pin_no        = 123
Balance       = 5000
History       = []
Daily_withdraw= 0
Count         = 0
Min_balance   = 500
Daily_limit   = 20000

count = 0

enter_pin = int(input("Enter the Pin no :"))
if enter_pin != enter_pin:
    print(("Wrong pin no"))
    exit()
else:
    print(f"Welcome {Customer_name} !")

while True:
    print("----------ATM MENU---------")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Transaction Summary")
    print("6. Change pin")
    print("7. Exit")

    choice = int(input("Enter the choice :"))

    if choice == 1:
        print("---------BALANCE---------")
        print("Account no :",Account_no) 
        print("Customer name :",Customer_name)   
        print("Balance :", Balance) 
        print("Daily Withdraw :",Daily_withdraw)   

    elif choice == 2:
        amount = int(input("Enter Deposit Amount :"))

        if amount <= 0 :
            print("Invalid Amount")
        else:
            Balance += Balance
            History.append(f"Deposit Rs.{amount}")
            count += 1
            print("Amount Deposit Successfully")
            print("New Balance :",Balance) 

    elif choice == 3:

        amount = int(input("Enter Withdraw Amount :"))
       
        if amount <= 0:
            print("Invalid Amount")

        elif amount > Balance:
            print("Insufficient Balance")

        elif (Balance - amount) < Min_balance:
            print(f"Cannot Withdraw, Minimum Balance Rs.{Min_balance} must be maintained")

        elif (Daily_withdraw + amount) > Daily_limit:
            print(f"Daily Limit Exceeded, Limit is Rs.{Daily_limit}")

        else:
            Balance -= amount
            Daily_withdraw += amount
            History.append(f"Withdrew Rs.{amount}")
            count += 1
            print("Amount Withdraw Successfully")
            print("New Balance :", Balance)

    elif choice == 4:

        receiver = int(input("enter receiver account number :"))
        amount = int(input("enter transfer amount :"))

        if amount <= 0:
            print("invalid amount")
        elif amount > Balance:
            print("insufficient balance")
        elif (Balance - amount) < Min_balance:
            print(f"cannot transfer, minimum balance Rs.{Min_balance} must be maintained")
        else:
            Balance -= amount
            History.append(f"Transferred Rs.{amount} to {receiver}")
            count += 1
            print(f"Rs.{amount} transferred to {receiver} successfully")
            print("new Balance :", Balance)

    elif choice == 5:

        print("------ TRANSACTION SUMMARY ------")
        if count == 0:
            print("no transactions available")
        else:
            for h in History:
                print(h)
            print("current balance :", Balance)

    elif choice == 6:

        old_pin = int(input("enter old PIN :"))

        if old_pin == Pin_no:
            new_pin = int(input("enter new 4 digit PIN :"))

            if new_pin >= 1000 and new_pin <= 9999:
                pin = new_pin
                History.append("PIN Changed")
                print("PIN changed successfully")
            else:
                print("PIN must be 4 digits")
        else:
            print("wrong old PIN")

    elif choice == 7:
        print("Thank you, Visit Again")
        break

    else:
        print("Invalid Choice")