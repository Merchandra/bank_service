# import uuid

# class Account:
#     def __init__(self,account_number,customer_name,mobile,balance):
#         self.account_number = account_number
#         self.customer_name = customer_name
#         self.mobile = mobile
#         self.balance = balance

# class Transaction:
#     def __init__(self,transaction_type,amount):
#         self.transaction_id=str(uuid.uuid4())[:8]
#         self.transaction_type = transaction_type
#         self.amount = amount 

# class BankService:
#     def __init__(self):
        
#         self.accounts = []
#         self.transactions = []

#     def create_account(self):
#       account_number= input("Enter Account Number:")
#       customer_name = input("Enter customer Name:")
#       mobile=input("Enter Mobile Number:")
#       balance=float(input("Enter Balance:"))

#       account = Account(
#           account_number,
#           customer_name,
#           mobile,
#           balance
#       )

#       self.accounts.append(account)

#       print("Account Created Successfully!")



#     def search_account(self):
#         account_number = input("Enter Account Number:")

#         for account in self.accounts:
#             if account.account_number == account_number:
#                 return account
#         print("Account not Found!")
#         return None
    
    
#     def deposit(self) :
#         account = self.search_account()

#         if account:
#             amount = float(input("Enter Deposit Amount:"))
#             account.balance +=amount

#             transaction = Transaction("Deposit",amount)
#         self.transactions.append(transaction)

#         print("Deposit Successfull!")

#     def withdraw(self):
#         account = self.search_account()

#         if account:
#             amount = float(input("Enter withdrawal Amount:"))

#             if amount<=account.balance:
#                 account.balance -=amount

#                 transaction=Transaction("Withdrawal",amount)
#                 self.transaction.append(transaction)

#                 print("Withdrawal Successful!")
#             else:
#                 print("Insufficient Balance!")


#     def transfer(self):
#         from_account=self.search_account()

#         if from_account:
#             to_number= input("Enter Receiver Account Number:")

#             for to_account in self.accounts:
#                 if to_account.account_number == to_number:

#                  amount = float(input("Enter Transfer Amount:"))

#                  if amount <= from_account.balance:

#                      from_account.balance -= amount
#                      to_account.balance += amount

#                      transaction=Transaction("Transfer",amount)

#                      self.transactions.append(transaction)

#                      print("Transfer Successful!")
#                  else:
#                      print("Insufficient Balance!")

#                      return 
                 
#                  print("Receiver Account Not Found!")

#     def check_balance(self):
#         account=self.search_account()
#         if account:
#             print("Name :",account.customer_name)
#             print("Balance:",account.balance)


#     def display_accounts(self):
#         if not self.accounts:
#             print("No Accounts Found!")

#         for account in self.accounts:

#          print("--------------------------")

#          print("Account Number:",account.account_number)
#          print("Mobile:",account.mobile)
#          print("Balance:",account.balance)


#     def view_transactions(self):
#         if not self.transactions:
#             print("No Transactions Found!")

#         for transaction in self.transactions:

#          print("----------------------------")
#         print("Transaction ID:",transaction.transaction_id)
#         print("Type:",transaction.transaction_type)
#         print("Amount:",transaction.amount)

# bank = BankService()

# while True:
#     print("\n--- BANK MANAGEMENT SYSTEM ---")
#     print("1.Create Account")
#     print("2.Deposit")
#     print("3.Withdraw")
#     print("4.Transfer")
#     print("5.Check Balance")
#     print("6.View All Accounts")
#     print("7.View Transaction")
#     print("8.Exit")

#     choice = input("Enter your choice:")

#     if choice == "1":
#         bank.create_account()

#     elif choice == "2":
#         bank.deposit()

#     elif choice == "3":
#         bank.withdraw()

#     elif choice == "4":
#         bank.transfer()

#     elif choice == "5":
#         bank.check_balance()

#     elif choice == "6":
#         bank.display_accounts()

#     elif choice == "7":
#         bank.view_transactions()

#     elif choice == "8":
#         print("Thank You!")
#         break

#     else:
#         print("Invalid Choice!")





    


        