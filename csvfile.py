# 1. Student.csv 
# RollNo,Name,Age,Department,Marks
# 101,Arun,20,CSE,85
# 102,Ram,21,ECE,92
# 103,Priya,20,IT,78
# 104,Kishore,22,CSE,88
# 105,Anu,21,ECE,95

# import csv
# file = open("Student.csv","r") 
# data = list(csv.DictReader(file))
# print(data)

# Read all records.
# print("All Recordes:")
# print(data)   

# Print first record.
# print("First Record:")
# print(data[0])

# Print last record.
# print("Last Record:")
# print(data[-1])

# Count students.
# print("Total Students:",len(data))

# Find highest marks.
# highest = max(data, key=lambda x:int(x["Marks"]))
# print("Highest Marks:",highest)

# Find lowest marks.
# lowest = min(data, key=lambda x:int(x["Marks"]))
# print("Lowest Marks:",lowest)

# Search student by RollNo.
# roll = input("Enter RollNo:")
# for i in data:
#     if i["RollNo"] ==# roll:
#         print(i)

# Search student by Name.
# print("All Recordes:")
# print(data)   

# Print first record.
# print("First Record:")
# print(data[0])

# Print last record.
# print("Last Record:")
# print(data[-1])

# Count students.
# print("Total Students:",len(data))

# Find highest marks.
# highest = max(data, key=lambda x:int(x["Marks"]))
# print("Highest Marks:",highest)

# Find lowest marks.
# lowest = min(data, key=lambda x:int(x["Marks"]))
# print("Lowest Marks:",lowest)

# Search student by RollNo.
# roll = input("Enter RollNo:")
# for i in data:
#     if i["RollNo"] == roll:
#         print(i)

# Search student by Name.
# name = input("Enter Name:")
# for i in data:
#     if i["Name"] == name:
#         print(i)

# Display only CSE students.
# for i in data:
#     if i["Department"] == "CSE":
#         print(i)

# Calculate average marks.
# total = sum(int(i["Marks"])for i in data)
# average = total / len(data)
# print("Average Marks:",average)



# Display only CSE students.
# for i in data:
#     if i["Department"] == "CSE":
#         print(i)

# Calculate average marks.
# total = sum(int(i["Marks"])for i in data)
# average = total / len(data)
# print("Average Marks:",average)


# -----------------------------------------------------------------------

# 2. Employee.csv
# ID,Name,Department,Salary,Experience
# 1,Amit,HR,35000,2 
# 2,Sara,IT,60000,5
# 3,Ravi,Finance,55000,4
# 4,Pooja,IT,72000,6
# 5,Kiran,Sales,40000,3

# Tasks
# import csv 
# file=open("Employee.csv","r")
# data=list(csv.DictReader(file))

# # Print employee names.
# for i in data :

#     print(i["Name"])

# # Find highest salary.

# highest=max(data,key=lambda i:int(i["Salary"]))
# print("Highest Salary:",highest)


# # Find average salary.

# total=sum(int(i["Salary"]) for i in data) 
# average =total/len(data) 
# print("Average Salary:",average)

# # Count IT employees.

# count=sum(1 for i in data if i["Department"])
# print("IT Employee:",count)



# # Search by department.
# dept=input("Enter Department:")
# for i in data:
#     if i ["Department"]==dept:
#         print(i)

# # Add a new employee.
# id=input("Enter ID:")
# name=input("Enter Name:")
# dept=input("Enter Department:")
# salary=input("Enter Salary:")
# exp=input("Enter Experience:")

    

# data.append({
#     "ID":id,
#     "Name":name,
#     "Department":dept,
#     "Salary":salary,
#     "Expericence":exp
# })

# # Update salary.
# id=input("Enter ID:")
# for i in data:
#     if i["ID"]==id:
#         i["Salary"]=input("Enter New Salary:")


# # Delete an employee.

# id=input("Enter ID:")
# for i in data:
#     if i["ID"]==id:
#         data.remove(i)
#         break

# ------------------------------------------------------------------------------------
# 3. Products.csv
# ID,Product,Category,Price,Stock
# 1,Laptop,Electronics,65000,20
# 2,Mouse,Accessories,500,150
# 3,Keyboard,Accessories,1200,80
# 4,Phone,Electronics,30000,45
# 5,Speaker,Audio,2500,35


# Tasks
# import csv
# file = open("Products.csv","r")
# data = list(csv.DictReader(file))
# file.close()

# # Most expensive product.
# highest = max(data,key = lambda i:
# int(i["Price"]))
# print(highest)

# # Cheapest product.
# lowest=min(data,key=lambda i:
# int(i["Price"]))
# print(lowest)

# # Out of stock products.
# for i in data:
#     if int(i["Stock"])==0:
#         print(i)

# # Products above ₹5000.
# for i in data:
#     if int(i["Price"])>5000:
#         print(i)

# # Total stock.
# total=sum(int(i["Stock"]) for i in data)
# print("Total Stock:",total)

# # Add a product.
# id=input("Enter ID:")
# name=input("Enter Product:")
# cat=input("Enter Category:")
# price=input("Enter Price:")
# stock=input("Enter Stock:")


# data.append({
#     "ID":id,
#     "Product":name,
#     "Category":cat,
#     "Price":price,
#     "Stock":stock
# })

# # Update stock.
# id=input("Enter ID:")
# for i in data:
#     if i["ID"]==id:
#         i["Stock"]=input ("Enter New Stock:")

# # Delete a product.
# id=input("Enter ID:")
# for i in data:
#     if i["ID"]==id:
#         data.remove(i)
#         break


# 4. Books.csv
# BookID,Title,Author,Price
# 1,Python Basics,Kishore,450
# 2,Java Guide,David,600
# 3,C Programming,James,350
# 4,Data Science,Raj,800


# import csv
# file=open("Books.csv","r")
# data=list(csv.DictReader(file))
# file.close()

# # Tasks
# # Search by title.



# # Search by author.
# author=input("Enter Author:")
# for i in data:
#     if i["Author"]==author:
#         print(i)


# # Highest priced book.
# highest=max(data,key=lambda i:
# int(i["Price"]))
# print("Highest Price:",highest)


# # Average price.
# total=sum(int(i["Price"])for i in data)
# average=total/len(data)
# print("Average Price:",average)

# # Add a new book.
# id=input("Enter Book ID:")
# title=input("Enter Title:")
# author=input("Enter Author:")
# price=input("Enter Price:")

# data.append({
#     "BookID":id,
#     "Title":title,
#     "Author":author,
#     "Price":price
# })

# 5. Movies.csv

# ID,Movie,Language,Year,Rating
# 1,Leo,Tamil,2023,8.2
# 2,Jailer,Tamil,2023,8.0
# 3,KGF,Kannada,2022,8.5
# # 4,RRR,Telugu,2022,8.7


# import csv
# file=open("Movies.csv","r")
# data=list(csv.DictReader(file))
# file.close()


# # Tasks
# # Movies after 2022.
# for i in data:
#     if int(i["Year"])>2022:
#         print(i)

# # Highest-rated movie.

# highest=max(data,key=lambda i:
# float(i["Rating"]))
# print("Highest Rated:",highest)

# # Tamil movies.
# for i  in data:
#     if i["Language"]=="Tamil:"
#     print(i)

# # Average rating.
# total=sum(float(i["Rating"]) for i
#           in data)
# average=total/len(data)
# print("Average Rating:",average)

# 6. Attendance.csv
# RollNo,Name,Present
# 101,Arun,Yes
# 102,Ram,No
# 103,Priya,Yes
# 104,Anu,Yes
# 105,Kishore,No

# import csv

# file = open("Attendance.csv", "r")
# data = list(csv.DictReader(file))
# file.close()

# # Count present students.
# present = 0

# for i in data:
#     if i["Present"] == "Yes":
#         present += 1

# print("Present:", present)


# # Count absent students.
# absent = 0

# for i in data:
#     if i["Present"] == "No":
#         absent += 1

# print("Absent:", absent)


# # List absent students.
# for i in data:
#     if i["Present"] == "No":
#         print(i["Name"])


# # Update attendance.
# roll = input("Enter RollNo:")

# for i in data:
#     if i["RollNo"] == roll:
#         i["Present"] = input("Enter Yes or No:")

# print(data)



# 7. Sales.csv
# Invoice,Customer,Amount
# 1001,Arun,1200
# 1002,Ram,850
# 1003,Kishore,2300
# 1004,Priya,1450

# import csv

# file = open("Sales.csv", "r")
# data = list(csv.DictReader(file))
# file.close()

# # Total sales.
# total = sum(int(i["Amount"]) for i in data)
# print("Total Sales:", total)

# # Highest bill.
# highest = max(data, key=lambda i: int(i["Amount"]))
# print("Highest Bill:", highest)

# # Lowest bill.
# lowest = min(data, key=lambda i: int(i["Amount"]))
# print("Lowest Bill:", lowest)

# # Average sales.
# average = total / len(data)
# print("Average Sales:", average)

# # Search invoice.
# invoice = input("Enter Invoice Number:")

# for i in data:
#     if i["Invoice"] == invoice:
#         print(i)