# 1.Create a Product class and store the details of one product.
# Input
# iPhone
# 80000
# Output
# Product = iPhone
# Price = 80000

# class product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

# p1=product("iphone",80000)

# print("Product=",p1.name)
# print("price=",p1.price)

    
# 2.Create 3 separate product objects for:
# iPhone
# Laptop
# Watch
# Print all product details.
# Output
# Product1 Details
# Product2 Details
# Product3 Details

# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

# p1=Product("iphone",80000)  
# p2=Product("Laptop",65000) 
# p3=Product("Watch",5000) 

# print("Product1 Details")
# print(p1.name,p1.price)

# print("Product2 Details")
# print(p2.name,p2.price)

# print("Product3 Details")
# print(p3.name,p3.price)

# 3.Create a method called display() inside the Product class.
# The method should print:
# Product Name
# Price
# Input
# Laptop
# 65000
# Output
# Product Name = Laptop
# Price = 65000

# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

#     def display(self):
#         print("Product Name=",self.name)
#         print("Price=",self.price)

# p1=Product("Laptop",65000)
# p1.display()
        



# 4.Create a method to calculate discounted price.
# Formula
# Discounted Price = Original Price - Discount Amount
# Input
# Price = 50000
# Discount = 10%
# Output
# Discounted Price = 45000

# class Product:
#     def __init__(self,price,discount):
#         self.price=price
#         self.discount=discount

#     def discount_price(self) :
#         discount_amount = self.price * self.discount /100
#         final_price = self.price - self.price - discount_amount

#         #                                                 5000 x 10 /100
#         #                                                  5000-50000=45000

#         print("Discount Price=",final_price)

# p1=Product(50000,10)
# p1.discount_price()



# 5.If stock is greater than 0:
# Print:
# In Stock
# Otherwise print:
# Out of Stock
# Input
# Stock = 5
# Output
# In Stock

# class Product:
#     def __init__(self,stock):
#         self.stock=stock

#     def check_stock(self):
#         if self.stock > 0:
#             print("In Stock")
#         else:
#             print("Out of Stock")
# p1=Product(5)
# p1.check_stock()
        


# 6.Create a Restaurant class and store one restaurant's details.
# Input
# Pizza Hut
# 4.5
# Output
# Restaurant = Pizza Hut
# Rating = 4.5

# class Restaurant:
#     def __init__(self,name,rating):
#         self.name=name
#         self.rating=rating

# r1= Restaurant("Pizza Hut",4.5) 

# print("Restaurnt =",r1.name)
# print("Rating =",r1.rating)


# 7.Create a method to calculate total bill amount.
# Input
# Burger = 120
# Pizza = 300
# Output
# Total Bill = 420

# class Restaurant:
#     def total_bill(self,burger,pizza):
#         total = burger + pizza
#         print("Total Bill=",total)

# r1=Restaurant()
# r1.total_bill(120,300)



# 8.Create a method to check delivery eligibility.
# Input
# Order Amount = 650
# Output
# Free Delivery Available

# class Restaurant:
#     def check_delivery(self,amount):
#         if amount >= 500:
#             print("Free Delivery Available")
#         else:
#             print("Delivey Charges Applicable")
# r1=Restaurant()
# r1.check_delivery(650)


# 9.Create a BankAccount class and store Rahul's account details.
# Input
# Rahul
# 5000
# Output
# Account Holder = Rahul
# Balance = 5000

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance

# b1 = BankAccount("Rahul",5000) 

# print("Account Holder=",b1.name) 
# print("Balance=",b1.balance)     

        

# 10.The method should add deposited amount to current balance.
# Input
# Current Balance = 5000
# Deposit Amount = 2000
# Output
# Updated Balance = 7000

# class BankAccount:
#     def __init__(self,balance):
#         self.balance = balance

#     def deposit(self,amount):
#         self.balance = self.balance + amount

#         print("Updated Balance=",self.balance)

# b1=BankAccount(5000)
# b1.deposit(2000)



# 11.The method should subtract withdrawal amount from balance.
# Input
# Balance = 7000
# Withdraw Amount = 3000
# Output
# Remaining Balance = 4000

# class BankAccount:
#     def __init__(self,balance):
#         self.balance = balance

#     def withdraw(self,amount):
#         self.balance = self.balance - amount

#         print("Remaining Balance =",self.balance)
# b1=BankAccount(7000)
# b1.withdraw(3000)
    
        
# 12. Check Insufficient Balance
# If withdrawal amount is greater than balance,
# print:
# Insufficient Balance
# Input
# Balance = 2000
# Withdraw Amount = 5000
# Output
# Insufficient Balance

# class BankAccount:
#     def __init__(self,balance):
#         self.balance = balance

#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("Insufficient")
#         else:
#             self.balance=self.balance - amount

#             print("Remaining Balance =",self.balance)

# b1=BankAccount(2000)
# b1.withdraw(5000)
        

# 13.Create a Student class and store one student's details.
# Input
# Arun
# 85
# Output
# Name = Arun
# Mark = 85

# class Student:
#     def __init__(self,name,mark):
#         self.name = name
#         self.mark = mark

# s1= Student("Arun",85)

# print("Name=",s1.name)
# print("Mark=",s1.mark)
        

# 14.Create a method to calculate grade based on marks.
# Conditions
# 90 and above → Grade A
# 75 to 89 → Grade B
# Below 75 → Grade C
# Input
# 92
# Output
# Grade A

# class Student:
#     def __init__(self,mark):
#         self.mark=mark

#     def grade(self):
#         if self.mark>=90:
#             print("Grade A")

#         elif self.mark >=75:
#             print("Grade B")

#         else:
#             print("Grade C")

# s1=Student(92)
# s1.grade()
        





# 15.If mark is below 40:
# Print:
# Fail
# Otherwise print:
# Pass
# Input
# 35
# Output
# Fail

# class Student:
#     def __init__(self,mark):
#         self.mark=mark

#     def result(self):
#         if self.mark < 40:
#             print("Fail")

#         else:
#             print("Pass")

# s1 = Student(35)   
# s1.result()    


# 16.Create a Movie class and store movie details.
# Input
# Leo
# 250
# Output
# Movie = Leo
# Ticket Price = 250

# class Movie:
#     def __init__(self, name, ticket_price):
#         self.name = name
#         self.ticket_price = ticket_price


# m1 = Movie("Leo", 250)

# print("Movie =", m1.name)

# print("Ticket Price =", m1.ticket_price)
        


# 17.Create a method to calculate total booking amount.
# Formula
# Total Amount = Ticket Price × Number of Seats
# Input
# Ticket Price = 250
# Seats = 3
# Output
# Total = 750

# class Movie:
#     def __init__(self, ticket_price):
#         self.ticket_price = ticket_price

#     def total_booking(self, seats):
#         total = self.ticket_price * seats

#         print("Total =", total)


# m1 = Movie(250)

# m1.total_booking(3)




# 18.If available seats are 0:
# Print:
# House Full
# Otherwise print:
# Seats Available
# Input
# Available Seats = 0
# Output
# House Full


# class Movie:
#     def __init__(self, seats):
#         self.seats = seats

#     def check_seats(self):
#         if self.seats == 0:
#             print("House Full")
#         else:
#             print("Seats Available")


# m1 = Movie(0)
# m1.check_seats()



# 19.Create an Employee class and store employee details.
# Input
# Kumar
# 35000
# Output
# Employee = Kumar
# Salary = 35000


# class Employee:

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary


# e1 = Employee("Kumar", 35000)

# print("Employee =", e1.name)

# print("Salary =", e1.salary)






# 20.Create a method to calculate employee bonus.
# Formula
# Bonus = Salary × Bonus Percentage / 100
# Input
# Salary = 40000
# Bonus Percentage = 10
# Output
# Bonus = 4000


# class Employee:
#     def __init__(self, salary):
#         self.salary = salary

#     def calculate_bonus(self, percentage):
#         bonus = self.salary * percentage / 100
#         print("Bonus =", bonus)


# e1 = Employee(40000)
# e1.calculate_bonus(10)





# 21.Create a method to calculate annual salary.
# Formula
# Annual Salary = Monthly Salary × 12
# Input
# Monthly Salary = 50000
# Output
# Annual Salary = 600000

# class Employee:
#     def __init__(self, salary):
#         self.salary = salary

#     def annual_salary(self):
#         annual = self.salary * 12
#         print("Annual Salary =", annual)


# e1 = Employee(50000)
# e1.annual_salary()