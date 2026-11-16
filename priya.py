
# 1. User Registration System
# A user enters their name during registration.
# Store the name and display a welcome message.
# Output Example
# Welcome Arun

# print("welcome arun")

# 2. Employee Information
# Store an employee's name and age and display them.
# Output Example
# Employee Name : Arun
# Employee Age  : 25
 
# print("Empoyee Name:Arun")
# print("Employee Age:25")
 
# 3. Grocery Billing System
# A customer buys 2 products.
# Store the prices and calculate the total bill.
# Example
# Rice  = 500
# Oil   = 250
# Total Bill = 750
# 
# rice=500
# oil=250
# total = rice + oil  
# print("Rice=",rice) 
# print("Oil=",oil)
# print("Total Bill=",total)/

# 4. Mobile Shop
# A customer buys a phone and a charger.
# Find the total purchase amount.

# phone = 20000
# charger = 1000
# total = phone + charger
# print("Total purcherse Amount=",total)

# 5. E-Commerce Discount
# An online store gives a flat ₹100 discount.
# Store product price and calculate final payable amount.
# Example
# Price = 1200
# Discount = 100
# Final Amount = 1100

# price = 1200
# discount = 100
# final_amount = price - discount
# print("price=" ,price)
# print("discount=",discount)
# print("final amount=",final_amount)

# 6. Cricket Scoring App
# A player hits 4 boundaries.
# Calculate total runs.
# Boundary = 4 runs
# Number of Boundaries = 4
# Total Runs = 16
 
# boundary = 4
# number_of_boundaries = 4
# total_runs = boundary * number_of_boundaries
# print("boundary =",boundary)
# print("number of boundaries=",number_of_boundaries)
# print("total runs =",total_runs)

# 7. OTP Verification System
# OTP received from API is stored as string.
# Convert it into integer.
# otp = "456789"

# otp="456789"
# otp_integer = int(otp)
# print("otp:",otp_integer)

# 8. Chat Application
# Take username from user and display:
# Hello Arun, Welcome to Chat App

# username = input("Enter your username:")
# print("Hello",username,"welcome to chat App")

# 9. Food Delivery App
# Calculate remaining amount after splitting bill among friends.
# Use modulus operator.
# Bill = 1000
# Friends = 3
# Remaining Amount = ?
 
# bill = 1000
# friends = 3
# remaining_amount = bill % friends 

# print("Remaining Amount:",remaining_amount)

# 10. Social Media Growth
# A page doubles followers every month.
# Find followers after 5 months using power operator
# Initial Followers = 100
 
# initial_followers=100
# months = 5 
# followers = initial_followers * (2**months)
# print("followers after 5 months:",followers)


# 11. Bank Simple Interest Calculator
# Customer deposits money in bank.
# Calculate simple interest.
# Inputs:
# Principal
# Rate
# Time
  
# principal = float(input("Enter Principal:"))
# rate = float(input("Enter Rate:"))
# time = float(input("Enter Time:"))

# simple_interest = (principal * rate * time ) / 100 

# print("Simple Interest:",simple_interest)

# 12. House Painting Cost
# A painter charges per square meter.
# Find area of wall.
# Length = 20
# Width = 15

# length = 20
# width = 15 
# area = length*width
# print("Area of wall:",area)

# 13. Land Measurement System
# A land surveyor wants area of circular park.
# Calculate area.
# Radius = 25 meter

# import math
# radius = 25 
# area=math.pi*radius**2
# print("Area of circular park:",area)
 

# 14. Weather App
# User enters temperature in Celsius.
# Convert to Fahrenheit.
# Example:
# 32°C → 89.6°F

# celsius = float(input("Enter temperature in Celsius:"))
# fahrenheit = (celsius*9/5)+32
# print("Temperature in Fahrenheit:",fahrenheit)

# 15. Logistics Company
# Truck travels 25 kilometers.
# Convert distance into meters.

# kilometers=25
# merters = kilometers*1000
# print("Kilometers=",kilometers)
# print("Meters=",merters)

# 16. Student Performance Dashboard
# Store marks of 5 subjects.
# Calculate average marks.
# Example:
# Math
# Science
# English
# Physics
# Chemistry 

# math=80
# science=75
# english=80
# computer=90
# social=70
# average=(math+science+english+computer+social)/5

# print("Average Marks:",average)

# 17. Wallet Transfer
# User A transfers money to User B.
# Swap balances using third variable.
# Wallet A = 500
# Wallet B = 1000
  
# wallet_a=500
# wallet_b=1000

# temp=wallet_a
# wallet_a = wallet_b
# wallet_b = temp

# print("Wallet A:",wallet_a)
# print("Wallet B:,wallet_b")

# 18. Game Character Position Swap
# Two players exchange positions.
# Swap values without using third variable.

# player_a = 10
# player_b = 20
# player_a,player_b = player_b,player_a
# print("Player A:",player_a)
# print("Player B:",player_b)

# 19. School Result Management System
# Store marks of 5 subjects.
# Calculate:
# Total Marks
# Percentage
# Average
# Display result card.
# Total Marks = ?
# Percentage = ?

# math=80
# science=75
# english=85
# computer=90
# social=70

# total = math + science + english + computer + social
# percentages = (total/500) * 100
# average = total/5


# print("_____RESULT CARD_____")
# print("Math;",math)
# print("Science:",science)
# print("English:",english)
# print("Computer:",computer)
# print("Social:",social)
# print("Total Marks:",total)
# print("Percentage:",percentages)
# print("Average:",average)



# 20. Video Streaming Platform
# Convert total video duration from seconds into:
# Hours
# Minutes
# Seconds
# Example:
# Video Length = 7384 seconds
# Output:
# 2 Hours
# 3 Minutes
# 4 Secondsmath=80
# seconds=7384 
# hours=seconds //3600
# seconds=seconds % 3600
# minutes = seconds// 60
# seconds = seconds%60

# print(hours,"Hours")
# print(minutes,"Minutes")
# print(seconds,"seconds")


# -----------------------------------------------------------------------------------------------
# a = 40
# b = 50
# a = a+b
# b = a-b
# a = a-b
# print(a)
# print(b)


# a =100
# b =60
# a = a+b
# b = a-b
# a = a-b
# print(a)
# print(b)

# while False:
    # print("hello")
    # print("end")


#  x =1
# while x <=5:
    # print(x)
    # x=x+1 

# x=2
# while x <=10:
#     print(x)
#     x=x+2

# count=1
# while count <=20 :
#     print(count)
#     count= count+2 

#1. Print numbers from 1 to N

# n = int(input("Enter N:"))
# x = 1
# while x<=n:
#  print(x)
#  x = x+1

# 2. Print numbers from 1 to N

# n = int(input("Enter N:"))
# x = 1
# while x<=n:
#     print(x)
#     x=x+1
 

# 3. Print numbers from N to 1

# n = int(input("Enter N:"))
# while n>=1:
#     print(n)
#     n = n-1

# 4.4.Print even numbers from 1 to 20
# x=2
# while x<=20:
#   print(x)
#   x=x+2

# 5.Print odd numbers from 1 to N
 
# n = int(input("Enter N:"))
# x=1
# while x<=n:
#     x=x+2

# 6.Print multiples of 3 up to 30

# x=3
# while x<=30:
#     print(x)
#     x=x+3

# 7.Print first N multiples of 7

# n=int(input("Enter N:"))
# i=1
# while i<=n:
#     print(i*7)
#     i+=1

# 8.Print squares from 1 to N

# n=10
# x=1
# while x<=10:
#     print(x ** 2)
#     x+=1

 


# 9.Print cubes from 1 to N

# n=10
# x=1
# while x<=10:
#     print(x**3)
#     x+=1

#10. print table of a number
# n=int(input("Enter N:"))
# x=1
# while x<=10:
#     print(n,"*",x,"=",n*x)
#     x+=1


# 11.Print numbers from 1 to N skipping multiples of 3

# n=20
# i=1
# while i<=20:
#     if i % 3 !=0:
#         print(i)
#     i+=1

# 12.Print numbers from 1 to N divisible by 4

# n =int(input("Enter N:"))
# i=1
# while i<=n:
#     if i % 4 ==0:
#         print(i)
#     i+=1

# 13.Print numbers from 1 to N where square is < 100
# n=20
# x=1
# while x<=20:
#     if x ** 2 <100:
#         print(x)
#     x+=1


# 14.Print numbers from N to 1 skipping even numbers

# n=int(input("Enter N:"))
# x=n
# while x >=1:
#     if x % 2 !=0:
#         print(x)
#     x-=1

# 15.Print first N triangular numbers
# n=int(input("Enter N:"))
# x=1
# while x<=n:
#     print( x *(x+1)//2)
#     x+=1



# -----------------count---------------------
# 1.Count even numbers from 1 to N

# n = int(input("Enter N:"))
# i=1
# count=0
# while i<=n:
#     if i % 2==0:
#         count+=1
#     i +=1
# # print("Count=",count)   

# # 2.Count odd numbers from 1 to N

# n=int(input("Enter N:"))
# i=1
# count=0
# while i<=n:
#     if i % 2==0:
#         count+=1
#     i+=1
# print("Count=",count)    


# 3.Count numbers divisible by 3 from 1 to N

# n=int(input("Enter N:"))
# i=1
# count=0
# while i<=n:
#     if i % 3==0:
#         count+=1
#     i+=1
# print(count)

# 4.Count numbers divisible by 5 from 1 to N
# n=int(input("Enter N:"))
# x=1
# count=0
# while x<=n:
#     if x % 5 ==0:
#        count +=1
#     x+=1
# print(count)    

    

# 5.Count numbers greater than 50 from 1 to 100
# n=100
# x=1
# count=0

# while x<=n:
#     if x > 50:
#         count+=1
#     x+=1
# print(count)
        
# 6.Count numbers divisible by both 3 and 5

# n=30
# x=1
# count=0

# while x<=n:
#     if x % 3 == 0 and x % 5 == 0:
#        count+=1
#     x+=1
# print(count)    

# 7.Count numbers not divisible by 4
# n=10
# x=1
# count=0

# while x <=10:
#     if x % 4!=0:
#         count+=1
#     x+=1
# print(count)        

# 8.Count numbers whose square is less than 200
# n=20
# x=1
# count=0
# while x <=n:
#     if x*x < 200:
#         count+=1
#     x+=1
# print(count) 

# 9.Count numbers between 1 and N divisible by 7

# n=30
# x=1
# count=0
# while x<=n:
#     if x%7==0:
#         count+=1
#     x+=1
# print(count)       
# 10.Count numbers from 1 to N that are prime candidates (not divisible by 2 or 3)
# n=10
# x=1
# count=0
# while x <=10:
#     if x % 2 !=0 and x % 3 !=0:
#         count+=1
#     x+=1
# print(count)        
# 11.Count numbers from 1 to N divisible by either 4 or 6
# n=12
# x=1
# count=0
# while x<=n:
#     if x%4==0 or x%6==0:
#         count+=1
#     x+=1
# print(count)        

# 12.Count numbers from 1 to N divisible by exactly one of 3 or 5
# n=15
# x=1
# count=0
# while x<=n:
#     if (x%3==0)!=(x%5==0):
#         count+=1
#     x+=1
# print(count)        

# 13.Count numbers whose cube is less than N
# n=30
# x=1
# count=0

# while x<=n:
#     if x * x * x < n:
#         count+=1
#     x+=1
# print(count)    


# 14.Count numbers from 1 to N whose square is even and also print even number
# n=10
# x=1
# count=0
# while x<=n:
#     if (x*x)%2==0:
#        print(x)
#     count+=1
#     x+=1    
       
# print("Count=",count)


# 15.Count numbers from 1 to N where i² + i is divisible by 2
# n=10
# i=1
# count=0
# while i<=n:
#     if (i * i + i)%2==0:
#         count+=1
#     i+=1
# print(count)        
# 
# ------------------------------------digit extraction---------------------------------------------------


# num=5782359
# count=0
# while num>0:
#     last=num%10
#     if last%2!=0:
#         count=1
#     num=num//10
# print(count)    



# 1.Find sum of digits of a number

# n=1234
# sum=0

# while n > 0:
#     digit =  n % 10
#     sum = sum + digit
#     n = n//10
# print(sum)   

# 2.Count digits of a number
# n= 1234
# count=0
# while n >0:
#     digit = n % 10
#     count+=1
#     n=n // 10
# print(count)  

# 3.Print digits of a number
# n=1234
# while n>0:
#     digit=n%10
#     print(digit)
#     n=n//10

# 4.Find product of digits
# n=123
# product=1
# while n>0:
#     digit = n % 10
#     product=product*digit
#     n=n//10
# print(product)    

# 5.Find largest digit
# n=7654
# largest=0
# while n>0:
#     digit=n%10

#     if digit > largest:
#         largest = digit

#     n=n//10
# print(largest)         
# 6.Reverse a number
# n=1234
# reverse=0

# while n>0:
#     digit=n%10
#     reverse=reverse*10+digit
#     n=n//10
# print(reverse)

# 7.Check if number is palindrome
#  n=121
# original=n
# reverse=0
# while n>0:
#     digit=n%10
#     reverse=reverse*10+digit
#     n= n//10
# if original==reverse :
#     print("Palindrome")   
# else:
#     print("Not Palindrome")    


# 8.Find smallest digit
# n=5832
# smallest=9

# while n>0:
#     digit=n%10

#     if digit < smallest:
#         smallest=digit

#     n=n//10  
# print(smallest)      

# 9.Count even digits
# n=123456789
# count=0

# while n>0:
#     digit=n%10

#     if digit % 2 ==0:
#        count+=1
#     n=n//10
# print(count)       

# 10.Count odd digits
# n=123456789
# count=0

# while n>0:
#     digit=n%10

#     if digit % 2 !=0:
#        count+=1
#     n=n//10
# print(count)       
# 11.Find sum of squares of digits
# n=123
# sum=0

# while n>0:
#     digit=n%10
#     sum=sum+digit*digit
#     n=n//10
# print(sum)   
# 12.Check Armstrong number
# n=1
# original=n
# sum=0

# while n>0:
#     digit=n%10
#     sum=sum+digit*digit*digit
#     n=n//10

# if sum == original:
#     print("Armstrong")  
# else:
#     print("Not Armstrong")

# 13.Check if digit sum is divisible by 3

# n=123
# sum=0

# while n>0:
#     digit=n%10
#     sum=sum+digit
#     n=n//10
# if sum%3==0:
#     print("Divisible by 3")    
# else:
#     print("Not Divisible by 3")   
# 14.Build number using even digits only
# n=123456
# result=0
# place=1

# while n>0:
#     digit=n%10

#     if digit % 2==0:
#         result = digit*place+result
#         place = place*10
#     n = n//10

# print(result)        

# 15.Find difference between largest and smallest digit
# n=5832
# largest=0
# smallest=9

# while n>0:
#     digit=n%10
#     if digit>largest:
#         largest=digit
#     if digit<smallest:
#         smallest=digit
#     n=n//10
# difference=largest-smallest
# print(difference)num         

# --------------------------------------------------------------------------------------------
# check 7 is prime number ?

# num=7
# isprime ="prime"
# for i in range (2,9):
#     if num % i==0:
#         isprime="not prime"
# print(isprime)       

# if it is notprime number count 1 ?

# num=9
# count=0
# for i in range (1,num+1):
#     if num % i == 0:
#         count+=1
# print (count) 
 
# if count==2:
#     print("prime")
# else:
#     print("not prime") 

# ----------------------------

# only print a prime number and count
# for i in range (2,11):
#     count=0
#     for j in range (1,11):
#         if i % j ==0:
#             count+=1
#     if count==2:
#         print(i)   
 
#----------------------------
# for i in range (2,50):
#     count=0
#     for j in range (1,i+1):
#         if i % j ==0:
#             count+=1
#     if count==2:
#         print(i)    
# -----------------------------
# for row in range (1,6):
#     for col in range (1,6):
#         if row==5 or col==1:
#             print("*",end="")
#         else:
#             print("",end="")
#         print()




# ---------patterns--------- 



# 1.print 5 rows of stars 
# for i in range(5):
#     print("*****")

# 2.Rectangle -3 rows,4 columns
# for row in range(3):
#     for col in range(4):
#         print("*",end="")
#     print()    

#3. Increaing Triangle

# for row in range(1,6):
#     for col in range(row):
#         print("*",end="")
#     print()    
# 
# 4.Decreasing Triangle

# for row in range (5,0,-1):
#     for col in range(row):
#         print("*",end="")
#     print()    

#5.Right-Aligned Triangle
 
# for row in range(1,6):
#     for space in range(5-row):
#          print(" ",end="")
#     for col in range(row):
#          print("*",end="")   
#     print()       

# 6.Number Triangle 
# for row in range(1,5):
#     for col in range(1,row+1):
#         print(col,end="")
#     print()    
# 7.Hollow patterns
# for row in range(1,6 ):
#     for col in range(1,6):
#         if row == 1 or row ==5 or col == 1 or col==5:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()        

# 8.pyramid 
# for row in range (1,5):
#     for space in range (4-row):
#         print(" ",end="") 
#     for col in range (2*row-1):
#         print("*" ,end="")
#     print()  
#   
# 9.Inverted pyramid
# for row in range (4,0,-1):
#     for space in range (4-row):
#         print(" ",end="") 
#     for col in range (2*row-1):
#         print("*" ,end="")
#     print()  

# 10.pattern with gaps
# 11.Diagonal pattern
# 12.conditinal nested loops 
# 13.Multi-variable Nested loops 
# ----------------------------------------------------------------------------------------------
# 1.Create a list of fruits.

# fruits = ["apple","papaya","banana"]
# print(fruits)

# 2.Print first element.
# numbers = [10,20,30,40,50,60,70,80]
# print(numbers[0])

# 3.Print last element.
# numbers = [10,20,30,40,50,60,70,80]
# print(numbers[-1])

# 4.Print middle element.
# numbers = [10,20,30,40,50,60,70,80]
# print(numbers[3:5])


# 5.Print first 3 elements.
# numbers = [10,20,30,40,50,60,70,80]
# print(numbers[:3])

# 6.Print last 2 elements.
# numbers = [10,20,30,40,50,60,70,80]
# print(numbers[-2:])

# 7.Print alternate elements.
# numbers = [10,20,30,40,50,60,70,80]
# print(numbers[::2])

# 8.Print reverse list.
# numbers = [10,20,30,40,50,60,70,80]
# print(numbers[::-1])

# 9.Print first half.
# numbers = [10,20,30,40,50,60,70,80]
# print(numbers[0:4])

# 10.Print second half.
# numbers = [10,20,30,40,50,60,70,80]
# print(numbers[4:])

# 11.Print elements from index 2 to 5.
# numbers = [10,20,30,40,50,60,70,80]
# print(numbers[2:6])

# 12.Update first student name.

# students = ["Ram", "Sam", "Arun", "Ravi", "Kumar"]
# students[0]="priya"
# print(students)

# 13.Change last city

# cities = ["Chennai", "Madurai", "Salem"]
# cities=["Chennai","Madurai","Salem"]
# cities[-1]="Coimbatore"
# print(cities)

# 14.Replace middle value of N length of list.
# numbers =[10,20,30,40,50,]
# middle = len(numbers)//2
# numbers.pop(middle)
# numbers.insert(middle,100)
# print(numbers)



# 15.Double all salaries.
# salaries = [20000, 30000, 40000, 50000]
# for i in range(len(salaries)):
#     salaries[i]=salaries[i]*2
# print(salaries) 
#     

# 16.Increase marks by 5.
# marks = [70, 80, 90, 60]
# for i in marks:
#     print(i+5)

# 17.Replace all negative values with 0.
# numbers = [10, -5, 30, -8, 20, -1]
# for i in range(len(numbers)):
#     if numbers[i]<0:
#         numbers[i]=0
# print(numbers)        

# 18.Change all "Pending" to "Completed".
# status = ["Pending", "Completed", "Pending", "Pending"]
# for i in range(len(status)):
#     if status[i]=="Pending":
#         status[i]="Competed"
# print(status)        


# 19.Replace zeros with 100
# numbers = [10, 0, 20, 0, 30]
# for i in range(len(numbers)):
#     if numbers[i]==0:
#         numbers[i]=100


# 20.Delete first item.
# numbers = [10, 20, 30, 40, 50]
# del numbers[0]
# print(numbers)


# 21.Delete last item.
# numbers = [10, 20, 30, 40, 50]
# del numbers[-1]
# print(numbers)

# 22.Remove student by name = Ram
# students = ["Ram", "Sam", "Ajay", "Ravi"]
# students.remove("Ram")
# print(students)

# 23.Remove all zeros.

# numbers = [10, 0, 20, 0, 30, 0, 40]
# while 0 in numbers:
#     numbers.remove(0)
# print(numbers)   
#  
# 24.Remove all negatives.
# numbers = [10, -5, 20, -8, 30, -1]
# for number in numbers[:]:
#     if number < 0:
#         numbers.remove(number)
# print(numbers)        


# 25.Empty list clear all.

# numbers = [10, 20, 30, 40]
# numbers.clear()
# print(numbers)

# 26.Search student Ram if found print found else not found

# students = ["Ram", "Sam", "Ajay", "Ravi"]
# if "Ram" in students:
#     print("Found")
# else:
#     print("not found")    

# 27.Count occurrences of 20.

# numbers = [10, 20, 30, 20, 40, 20]
# print(numbers.count(20))

# 28.Find index of first occurrence 20.
# numbers = [10, 20, 30, 20, 40]
# print(numbers.index(20))

# 29.Find index of last occurrence 20.

# numbers = [10, 20, 30,20,40,20]
# numbers[::-1].index(20)
# print(len(numbers)-1)

# 30.Check 20 is duplicate if print duplicate exists or not duplicate exits.
# numbers = [10, 20, 30, 20]
# if numbers.count(20)>1:
#     print("Duplicate exists")
# else:
#     print("Not duplicate")    

# 31.Add student Arun in list

# students = ["Ram", "Sam", "Ajay"]
# students.append("Arun")
# print(students)

# 32.Insert city

# cities = ["Chennai", "Madurai", "Salem"]
# cities.insert(1,"chengapattu")
# print(cities) 

# 33.Merge two classes

# class1 = ["Ram", "Sam", "Ajay"]
# class2 = ["Ravi", "Kumar", "Arun"]
# class1.extend(class2)
# print(class1)

# 34.Build list dynamically

# numbers=[]
# for i in range(1,6):
#     numbers.append(i)
# print(numbers)    

# 35.print highest mark
# marks = [75, 90, 65, 80, 85]
# print(max(marks))

# 36.Sort students

# students = ["Ram", "Ajay", "Sam", "Ravi"]
# students.sort()
# print(students)

# 37.Sort by length

# names = ["Ajay", "Christopher", "Sam", "Ram", "Vijay"]
# names.sort(key=len)
# print(names)nums = [10, -5, 25, 16, 7, 20, 9, 36, 1

# 38.Descending order of marks
# marks = [75, 90, 65, 80, 85]
# marks.sort(reverse=True)
# print(marks)

# 39.Second highest 

# marks = [75, 90, 65, 80, 85]
# marks.sort(reverse=True)
# print(marks[1])


# 40.Third smallest
# numbers = [45, 12, 78, 30, 20, 5]
# numbers.sort(reverse=True)
# print(numbers[2])

# 1.Print prime numbers
                                                                         
# nums=[3,6,4,5,7,8,2]
# for num in nums:
#     count=0
#     for i in  range(2,num):
#         if num%i==0:
#             count+=1
#     if count==0:
#         print(num)         


# 2.Count duplicates
# nums = [10, -5, 25, 16, 7, 20, 9, 36, 15, -8, 20, 0, 7]
# count=0
# for n in range(len(nums)):
#         for i in range(n+1,len(nums)):
#          if nums[n] == nums[i]:
#             count+=1
#             break
# print(count)            

            



#  3.Sum of second half


# numbers = [10, -5, 25, 16, 7, 20, 9, 36, 15, -8]
# half=len(numbers)//2
# sum=0
# for i in range(half,len(numbers)):
#     sum+=numbers[i]
# print(sum)    




# 4.Second Largest
# numbers = [10, 45, 23, 78, 56, 91, 12, 34, 67, 5]
# numbers.sort()
# print(numbers[-2])



# 5.Rotate Left by One
# numbers = [10, 20, 30, 40, 50]
# left = numbers.pop(0)
# numbers.append(left)

# print(numbers)

# 6.Rotate Left by K
# numbers = [10, 20, 30, 40, 50]

# k = 2

# for i in range(k):
#     left = numbers.pop(0)
#     numbers.append(left)
# print(numbers)    


# 41.Find employees whose salary is greater than 40000.

# employees = [
#     ["Arun", 35000],
#     ["Rahul", 45000],
#     ["Anu", 50000]
#  ]
# def find_employees(employees):
#    for employee in employees:
#       if employee[1] > 40000:
#          print(employee[0])

# find_employees(employees)  


# 42.Find products that are out of stock.
# products = [
#     ["Laptop", 5],
#     ["Mouse", 0],
#     ["Keyboard", 10]
# ]

# for product in products:
#     if product[1] == 0:
#         print(product[0])


# 43.Print every element.
# matrix = [
#     [1,2],
#     [3,4]
# ]

# for row in matrix:
#     for value in row:
#         print(value)


# 44.Calculate the sum.
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]


# total = 0

# for row in matrix:
#     for value in row:
#         total = total + value

# print(total)



# 45.Count present students.
# attendance = [
#     ["Arun","Present"],
#     ["Rahul","Absent"],
#     ["Anu","Present"]
# ]
# count = 0

# for student in attendance:
#     if student[1] == "Present":
#         count = count + 1

# print(count)


# 46.Search today's subject.
# timetable = [
#     ["Monday","Math"],
#     ["Tuesday","Science"],
#     ["Wednesday","English"]
# ]
# today = "Tuesday"

# for day in timetable:
#     if day[0] == today:
#         print(day[1])


# 47.Find highest scorer.
# players = [
#     ["Virat",80],
#     ["Rohit",120],
#     ["Dhoni",65]
# ]

# print(players[1][0])


# 48.Calculate total balance.
# transactions = [
#     ["Deposit",5000],
#     ["Withdraw",2000],
#     ["Deposit",3000]
# ]
# balance = 0

# for transaction in transactions:
#     if transaction[0] == "Deposit":
#         balance = balance + transaction[1]
#     else:
#         balance = balance - transaction[1]

# print(balance)


# 49.Calculate total bill.
# shopping = [
#     ["Laptop",50000],
#     ["Mouse",800],
#     ["Keyboard",1500]
# ]

# total = 0

# for item in shopping:
#     total = total + item[1]

# print(total)


# 50.Flatten Nested List
# matrix = [
#     [1,2],
#     [3,4],
#     [5,6]
# ]
# ex:[1,2,3,4,5,6]

# result = []

# for row in matrix:
#     for value in row:
#         result.append(value)

# print(result)
# -------------------------------------------------------------------------------------------------------------------
# string

# 1.Print only vowels 

# text = "Python"

# for ch in text:
#     if ch.lower() in "aeiou":
#         print(ch)



# 2.Print only consonants
# text = "Python"
# for ch in text:
#     if ch.lower()  not in "aeiou":
#         print(ch)



# 3.Print ASCII values
# text = "Python"

# for ch in text:
#     print(ord(ch))

# 4.Repeats a string 3 times.
# text = "Hi"
# print(text * 3 )


# 5.Convert to uppercase

# text = "python programming"
# print(text.upper())

# 6.Convert to lowercase

# text = "PYTHON PROGRAMMING"
# print(text.lower())


# 7.Input:course = "python full stack development"
# Output : Python Full Stack Development

# course="Python Full Stack Development"
# print(course.title())

# 8.Input: sentence = "welcome to python programming"
# Output : Welcome to python programming
 
# sentance="welcome to python programming"
# print(sentance.capitalize())

# 9.Input:text = "Python Full Stack"
# Output : pYTHON fULL sTACK

# text="Python Full Stack"
# print(text.swapcase())

# 10.Find "@" index
# email = "arun@gmail.com"

# name="arun@gmail.com"
# print(name.index("@"))

# 11.Replace spaces
# text = "Python Full Stack"
# Output :Python_Full_Stack

# text = "Python Full Stack"
# print(text.replace(" ","_"))

# 12.Split CSV
# csv = "101,Arun,Python"
# output : ['101', 'Arun', 'Python']

# csv = "101,Arun,Python"
# print(csv.split(","))


# 13.Employee Details

# name = "Rahul"
# designation = "Software Engineer"
# salary = 60000

# print(f"Employee:{name},Designation:{designation},Salary:{salary}")


# print:Employee: Rahul, Designation: Software Engineer, Salary: ₹60000



# 14.GST Bill
# product = "Laptop"
# price = 50000
# gst = 18

# gst_amount= price*gst/100
# total=price+gst_amount

# print(f"Product     : {product}")
# print(f"Price       : ₹{price}")
# print(f"GST         : {gst}%")
# print(f"GST Amount  : ₹{gst_amount:.2f}")
# print(f"Total       : ₹{total:.2f}")



# Output:
# Product     : Laptop
# Price       : ₹50000
# GST         : 18%
# GST Amount  : ₹9000.00
# Total       : ₹59000.00



# 1.Count Digits
# text = "Python Programming 2026!"
# count=0

# for char in text:
#     if char.isdigit():
#         count+=1
# print(count)        



# 2.Count Special Characters
# Special characters are characters that are not alphabets, digits, or spaces.

# text = "Python Programming 2026!"
# count=0

# for char in text:
#     if not char.isalnum()and not char.isspace():
#         count+=1
# print(count)       



# 3.Count Sentences
# Assume sentences end with ., !, or ?.

# text = "Python is easy. Java is powerful! Learn AI?"
# count=0
# for ch in text:
#     if ch=='.' or ch == '!' or ch =='?':
#         count+=1
# print(count)         

# 4.Find Longest Word
# text = "Python Programming Language"
# words = text.split()
# longest=""

# for word in words:
#     if len(word) > len(longest):
#         longest=word    
# print(longest)        


# 5.Remove Duplicates
# text = "programming"
# Output : progamin

# text = "programming"
# result=""
# for ch in text:
#     if ch not in result:
#         result+=ch
# print(result)        


# 6.Show only the last four digits.
# phone = "9876543210"
# Output :******3210

# phone = "9876543210"
# result="*" *(len(phone)-4) +phone[-4:]
# print(result)

# 7. write an Function to check Palindrome
# A palindrome reads the same forwards and backwards.
# Examples: madam

# def palindrome (text):
#     if text ==text[::-1]:
#         return True
#     else:
#         return False
    
# print(palindrome("madam"))

  


# 8. write an Function to check Anagram
# Two strings are anagrams if they contain the same letters in a different order.
# Examples : listen → silent ,heart → earth

# def anagram(text1,text2):
#     if sorted(text1.lower())== sorted(text2.lower()):
#         return True
#     else:
#         return False
# print(anagram("listen","silent")) 
# print(anagram("heart","earth"))




# 9.Function for Email Validation

# Simple Rules
# Must contain "@"
# Must contain "."

# def validate_email(email):
#     if "@" in email and "." in email:
#         return True
#     else:
#         return False

# print(validate_email("user@gmail.com"))
# print(validate_email("usergmailcom"))

# 10.Function for Strong Password
# Rules
# Minimum 8 characters
# At least one uppercase letter
# At least one lowercase letter
# At least one digit
# At least one special character

# password = "PRiya@$06" 
# if len(password) >= 8 :
#     any(c.upper() for c in password)  
#     any(c.lower() for c in password)
#     any(c.isdigit() for c in password)
#     any(c.isalnum() for c in password)
#     print("strong password")
# else:
#     print("not strong password")






# 11.IPv4 Validation 
# Rules
# Four parts
# Each between 0 and 255

# ip = "192.168.1.100"



# def validate_ip(ip):
#     parts = ip.split(".")

#     if len(parts) != 4:
#         return False

#     for part in parts:
#         if not part.isdigit():
#             return False

#         if int(part) < 0 or int(part) > 255:
#             return False

#     return True

# ip = "192.168.1.100"

# print(validate_ip(ip))







# 1.Largest Palindrome Substring
# text = "babad

# def largest_palindrome(text):
#     longest = ""

#     for i in range(len(text)):
#         for j in range(i + 1, len(text) + 1):
#             substring = text[i:j]

#             if substring == substring[::-1]:
#                 if len(substring) > len(longest):
#                     longest = substring

#     return longest

# text = "babad"
# print(largest_palindrome(text))



# 2.Run-Length Encoding
# Compress repeated characters.
# Example aaabbcccc becomes a3b2c4

# text = "aaabbcccc"
# result = ""
# count = 1 
# for i in range(1, len(text)):
#     if text[i] == text[i - 1]:
#         count += 1
#     else:   
#         result += text[i - 1] + str(count)
#         count = 1
# result += text[-1] + str(count)
# print(result)


# 3.Caesar Cipher
# Shift every letter by 3 positions.
# text = "ABC"
# Output
# DEF   




# 4.Decode Run Length Encoding
# From a3b2c4  to aaabbcccc



# 5.ROT13 rotates each alphabetic character by 13 positions. Applying it twice returns the original text.
# text = "HELLO"
# Output : URYYB

# -------tuple---------
# 1.Create a tuple of vowels.

# vowels=('a','e','i','o','u')
# print(vowels)

# 2.Repeat Tuple Three Times
# numbers = (10, 20)
# print(numbers*3)




# 3.Unpack Employee Details
# employee = (
#     1001,
#     "Rahul",
#     "Developer",
#     65000
# )

# employee = (
#     1001,
#     "Rahul",
#     "Developer",
#     65000
# )

# emp_id, name, role, salary = employee

# print("Employee ID:", emp_id)
# print("Name:", name)
# print("Role:", role)
# print("Salary:", salary)


# 4.Print student Name and Marks
# students = (
#     ("Arun",95),
#     ("Rahul",88),
#     ("Anu",99) 
# )

# for student in students:
#     print("Name:", student[0])
#     print("Marks:", student[1])

# 5.Change Student Name

# student = ("Arun", 22, "Python")
# student_list = list(student)
# student_list[0] = "Rahul"
# student = tuple(student_list)
# print(student)

# 
# --------------------------------------------------------------------------------------------


# 1.Multiply by 100
# numbers = [1, 2, 3, 4]
# # o/p : [100,200,300,400]

# print(list(map(lambda num:num*100,numbers)))



# 2.Find length of every word
# words = ["apple", "python", "java"]
# o/p : [5,6,4]

# print(list(map(lambda word:len(word),words)))

# 3.Get first character
# words = ["apple", "banana", "mango"]
# Output: ['a', 'b', 'm']

# print(list(map(lambda word:word[0] ,words)))



# 4.Add "Mr. " before every name
# names = ["Ajay", "Ravi", "Kumar"]
# Output: ['Mr. Ajay', 'Mr. Ravi', 'Mr. Kumar']
# print(list(map(lambda name:"Mr."+name,names)))


# 5.Add 18% GST to product prices
# prices = [100, 500, 1000]
# Output: [108, 540, 1080]
# print(list(map(lambda price:price*1.08,prices)))


# 6.Calculate student result — Pass or Fail
# marks = [80, 30, 65, 25, 90]
# Output: ['Pass', 'Fail', 'Pass', 'Fail', 'Pass']
# print(list(map(lambda mark:"pass" if mark>=35 else "fail",marks)))



# 7.Append " kg"
# weights=[10,20,30]
# Output: ['10 kg', '20 kg', '30 kg']
# print(list(map(lambda weight: str(weight)+"kg",weights )))

# 8.Remove empty strings
# values = ["Python", "", "Java", ""]
# Output: ['Python', 'Java']
# print(list(filter(lambda value:value != "",values)))



# 9.. Filter positive numbers
# numbers = [-10, 5, -3, 0, 8, 12]
# Output: [5, 8, 12]
# print(list(filter(lambda number:number > 0 ,numbers)))



# 10.Words longer than 5 characters
# words = ["apple", "banana", "cat", "python"]
# Output: ['banana', 'python']
# print(list(filter(lambda word:len(word)>5,words )))


# 11.Numeric strings
# values = ["123", "abc", "456", "a12"]
# Output: ['123', '456']

# print(list(filter(lambda value:value.isdigit(),values)))

# 12.Emails containing "@"
# emails = [
#      "arun@gmail.com",
#      "invalidemail.com",
#      "ravi@yahoo.com"
# ]
# # Output: ['arun@gmail.com', 'ravi@yahoo.com']

# print(list(filter(lambda email:"@" in email,emails)))

# 13.Positive bank transactions
# transactions = [-500, 1000, -200, 3000, 500]
# Output: [1000, 3000, 500]

# print(list(filter(lambda transaction:transaction > 0,transactions)))


# 14.Digit sum greater than 10
# numbers = [12, 29, 123, 99, 45]
# # Output: [29, 99]

# def digit_sum(n):
#     total=0
#     while n>0:
#         total+=n%10
#         n//=10 
#     return total
# print(list(filter(lambda number:digit_sum(number)>10,numbers)))


# 15.Filter expensive products and apply a 10% discount
# Assume products above ₹1000 are expensive.
# prices = [500, 1500, 800, 2000, 3000]
# # Output: [1350.0, 1800.0, 2700.0]


# expensive=list(filter(lambda price:price>1000,prices))
# discount=list(map(lambda price:price*0.9,expensive))
# print(discount)


# 16.Find total cricket score
# scores = [45, 60, 10, 80, 25]
# # Output: 195


# from functools import reduce
# scores = [45, 60, 10, 80, 25]
# print(reduce(lambda a,b:a+b,scores))

# 17.Find difference by reducing left to right
# numbers = [100, 20, 10, 5]
# Output: 65

# from functools import reduce
# numbers=[100,20,10,5]
# print(reduce(lambda a,b:a-b,numbers))


# 18.Join words with -
# words = ["python", "java", "react"]
# Output: 'python-java-react'

# words = ["python", "java", "react"]
# print("-" .join(words))



# 19.Find final balance after applying transaction values
# initial_balance = 10000
# transactions = [2000, -500, 3000, -1000]
# Output: 13500

# from functools import reduce
# initial_balance=1000
# transactions = [2000, -500, 3000, -1000]

# final_balance=reduce(lambda a,b:a+b,transactions,initial_balance)
# print(final_balance)

# 20.Filter salaries above ₹30,000 → increase by 10% → find payroll total
# Output: 145000
# salaries = [20000, 35000, 50000, 25000, 60000]
# print(sum(map(lambda salarie:salarie*1.1,filter(lambda salarie:salarie>30000,salaries))))



# 21.Filter available product prices → discount them → find cheapest
# Assume prices greater than 0 are available and discount is 10%.
# prices = [500, 0, 1500, -100, 800]
# # Output: 450.0
# print(min(map(lambda price:price *0.9,filter(lambda price: price > 0,prices))))




# ------------------------------------------------------------------------------------------------------
# dictoinary


# 1.Return "Unknown" for a Missing City
# student = {
#     "name": "Arun",
#     "age": 22
# }

# print(student.get("city","unknown"))


# 2.Check Whether a Product "Laptop" Exists Among Values

# product = {
#     "id": 101,
#     "name": "Laptop",
#     "price": 50000
# }

# print("Laptop" in product.values())


# 3.Display All Key-Value Pairs
# 
# student = {
#     "name": "Ajay",
#     "age": 22,
#     "course": "Python"
# }
# print(student.items())



# 4.Delete All Optional Fields


# student = {
#     "name": "Arun",
#     "age": 22,
#     "email": "arun@gmail.com",
#     "city": "Chennai"
# }
# optional_fields = ["email", "city"]

# for i in optional_fields:
#     del student[i]
# print(student)

# 5.Update Stock After a Purchase


# product = {
#     "name": "Laptop",
#     "price": 50000,
#     "stock": 10
# }
# quantity = 3

# product["stock"]=product["stock"]-quantity
# print(product)


# 6.Find the Average of Dictionary Values

# marks = {
#     "Tamil": 80,
#     "English": 70,
#     "Maths": 90
# }

# average = sum(marks.values())/len(marks)
# print(average)


# 7.Find the Largest Value


# marks = {
#     "Tamil": 80,
#     "English": 70,
#     "Maths": 95
# }
# print(max(marks.values()))


# 8.Find the Key with the Largest Value

# marks = {
#     "Tamil": 80,
#     "English": 70,
#     "Maths": 95
# }
# # Output:
# # Subject: Maths
# # Mark: 95

# subject=max(marks,key=marks.get)
# print("Subject:",subject)
# print("Marks:",marks[subject])




# 9.Print Only Keys Whose Values Are Positive

# numbers = {
#     "a": 10,
#     "b": -5,
#     "c": 20,
#     "d": -10
# }
# print(list(filter(lambda X:numbers[X]>0,numbers)))


# 10.Count Failed Students


# students = {
#     "Ram": 80,
#     "Sam": 30,
#     "Arun": 65,
#     "Ravi": 25
# }




# 11.Print Keys Longer Than Five Characters

# data = {
#     "name": "Ram",
#     "course": "Python",
#     "address": "Chennai",
#     "age": 22
# }
# print(len(list(filter(lambda x:len(x) > 5,data))))

# 12.Find Average Nested Marks

# student = {
#     "name": "Arun",
#     "marks": {
#         "Tamil": 80,
#         "English": 75,
#         "Maths": 95
#     }
# }
# m=student["marks"].values()
# print(sum(m)/len(m))


# 13.Find the Highest-Scoring Student
# students = {
#     101: {
#         "name": "Ram",
#         "mark": 80
#     },

#     102: {
#         "name": "Sam",
#         "mark": 70
#     },

#     103: {
#         "name": "Arun",
#         "mark": 95
#     }
# }
  
# print(max(students.values(),key=lambda x:x["mark"])["name"])



# 14.Create Numbers and Parity Labels using loop
# ex:{1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd'}







# 15.Create Products Apply a 10% Discount to Every Price
# products = {
#     "Laptop": 50000,
#     "Mouse": 1000,
#     "Keyboard": 2000
# }
# # Output:
# # {
# #     'Laptop': 45000.0,
# #     'Mouse': 900.0,
# #     'Keyboard': 1800.0
# # }

# print({k:(lambda x:x*0.9)(v) for k,v in products.items()})




# 16.Keep Only Available Products
# products = {
#     "Laptop": 10,
#     "Mouse": 0,
#     "Keyboard": 5,
#     "Monitor": 0
# }
# print(dict(filter(lambda X:X[1] > 0,products.items())))


# 17.Keep Only Active Users

# users = {
#     "Ram": True,
#     "Sam": False,
#     "Arun": True,
#     "Ravi": False
# }

# print(dict(filter(lambda X:X[1],users.items())))

# 18.Keep Only Products Below a Target Price

# products = {
#     "Laptop": 50000,
#     "Mouse": 500,
#     "Keyboard": 1500,
#     "Monitor": 12000
# }
# target = 10000
# print(dict(filter(lambda X:X[1] < target,products.items())))


# 19.Swap Keys and Values
# student = {
#     "name": "Arun",
#     "city": "Chennai",
#     "course": "Python"
# }

# print({v:k for k,v in student.items()})




#  1.Count Frequency of Each Character
# text = "banana"
# Output: {'b': 1, 'a': 3, 'n': 2}

# fre={
  
#  }
# for i in text:
#     if i in fre:
#         fre[i]+=1
#     else:
#         fre[i]=1
# print(fre)       


# 2.Count Frequency of Digits
# text = "1122333115"
# # {'1': 4, '2': 2, '3': 3, '5': 1}
# fre={

# }
# for i in text:
#     if i in fre:
#         fre[i]+=1
#     else:
#         fre[i]=1
# print(fre)        



# 3.Find the Most Frequent Number

# numbers = [10, 20, 10, 30, 20, 10]
# fre={}
# for i in numbers:
#     if i in fre:
#         fre[i]+=1
#     else:
#         fre[i]=1   
# print(max(fre,key=fre.get))         


# 4.Find All Duplicate Values Using Frequencies
# numbers = [10, 20, 10, 30, 20, 40]
# # Output :[10, 20]
# freq={}
# for i in numbers:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# result=[i for i in freq if freq[i] > 1] 
# print(result)       


# 5.Find the First Non-Repeated Character
# text = "swiss"
# First Non-Repeated: w


# text="swiss"
# for i in text:
#     if text.count(i)==1:
#         print(i)
#         break


# 6.Two Sum Using a Dictionary
# numbers = [2, 7, 11, 15]
# target = 9

# seen={}
# for i in numbers:
#     diff=target-i

#     if diff in seen:
#         print(seen[diff],i)
#         break
#     seen[i]=i


# 7.Store the Last Index of Every Value

# numbers = [10, 20, 10, 30, 20]
# result={}
# for i in range(len(numbers)):
#     result[numbers[i]]=i
#     print(result)



# 8.Group Values by Category

# products = [
#     ("Laptop", "Electronics"),
#     ("Shirt", "Clothing"),
#     ("Mouse", "Electronics"),
#     ("Jeans", "Clothing")
# ]
# output:{
#     'Electronics': ['Laptop', 'Mouse'],
#     'Clothing': ['Shirt', 'Jeans']
# }



# 9.Group Words by Length
# words = ["cat", "dog", "python", "java", "apple"]
# Output:
# {
#     3: ['cat', 'dog'],
#     6: ['python'],
#     4: ['java'],
#     5: ['apple']
# }
# 10.Find the First Repeated Character
# text = "programming"
# First Repeated: r


# 11.Find Duplicate Words in a Sentence
# text = "python java python c java python"


# 12.Check Whether Two Strings Are Anagrams
# Anagrams contain the same characters with the same frequencies.
# Example:
# listen
# silent



# --------------------------------------------------------------------------------------------------------------
# .........SET........



# 1.Convert a String to a Set
# text = "banana"

# print(set(text))



# 2.Find Unique Cities from Customer Data


# cities = [
#     "Chennai",
#     "Madurai",
#     "Chennai",
#     "Coimbatore",
#     "Madurai"
# ]
# print(set(cities))



# 3.Find Unique Digits in a Number

# number = 1122334455
# print(set(str(number)))



# 4.Find the Number of Unique Words
# text = "python java python c java python"

# print(len(set(text.split())))




# 5.Unblock a User sam
# blocked_users = {"Ram", "Sam", "Ravi"}
# blocked_users.remove("Sam")
# print(blocked_users)



# 6.Find All Students from Two Classes
# class_a = {"Ram", "Sam", "Arun"}
# class_b = {"Arun", "Ravi", "Kumar"}
# print(class_a | class_b)



# 7.Find Common Students in Two Courses
# class_a = {"Ravi", "Sam", "Arun"}
# class_b = {"Arun", "Ravi", "Kumar"}
# print(class_a & class_b)




# 8.Find Products Available Only in Shop A
# shop_a = {"Laptop", "Mouse", "Keyboard"}
# shop_b = {"Mouse", "Monitor"}
# print(shop_a - shop_b)

 

# 9.Find Users Who Registered but Did Not Pay
# registered = {"Ram", "Sam", "Anu", "Ravi"}
# paid = {"Sam", "Ravi"}
# print(registered - paid)



# 10.Find Skills Unique to Either Developer
# developer_a = {"Python", "React", "SQL"}
# developer_b = {"Java", "React", "AWS"}

# print(developer_a ^ developer_b )


# 11.Check Whether All Required Skills Are Present
# required = {"Python", "SQL"}
# candidate = {"Python", "SQL", "React", "AWS"}

# print(required.issubset(candidate))



# 12.Count Distinct Elements
# numbers = [10, 20, 10, 30, 20, 40]

# print(len(set(numbers)))


# 13.Find the First Repeated Element
# numbers = [10, 20, 30, 20, 40, 10]
# # Output : 20

# s=set()
# for num in numbers:
#     if num in s:
#         print(num)
#         break
#     s.add(num)

 
# 14.Find All Duplicate Values
# numbers = [10, 20, 30, 20, 40, 10, 20]
# # Output :{10, 20}

# s=set()
# duplicates=set()

# for num in numbers:
#     if num in s:
#         duplicates.add(num)

#     else:
#         s.add(num)
# print(duplicates)       
# 
# 
# 
#      
# 1.Two Sum Existence Check Using a Set
# numbers = [2, 7, 11, 15]
# target = 9


# # Check whether any two numbers produce 9.


# s=set()
# for num in numbers:
#     if target - num in s:
#         print(True)
#         break
#     s.add(num)
# else:
#     print(False)    





# 2.Find the Longest Consecutive Sequence
# Example:
# [100, 4, 200, 1, 3, 2]
# Longest consecutive sequence:
# 1, 2, 3, 4
# Length:4
# numbers = [100, 4, 200, 1, 3, 2]

# s = set(numbers)
# longest = 0

# for num in s:
#     if num - 1 not in s:
#         count = 1

#         while num + count in s:
#             count += 1

#         longest = max(longest, count)

# print(longest)


# 3.Find Missing Numbers from a Range
# numbers = [1, 2, 4, 6, 7]
# start = 1
# end = 7
# Output :{3, 5}

# numbers = [1, 2, 4, 6, 7]

# start = 1
# end = 7

# missing = set()

# for num in range(start, end + 1):
#     if num not in numbers:
#         missing.add(num)

# print(missing)


# 4.Find Intersection of Multiple Arrays
# array1 = [10, 20, 30, 40]
# array2 = [20, 30, 40, 50]
# array3 = [30, 40, 60]
# xOutput :{30, 40}


# array1 = [10, 20, 30, 40]
# array2 = [20, 30, 40, 50]
# array3 = [30, 40, 60]

# result = set(array1) & set(array2) & set(array3)
# --------------------------------------------------------------------------------------------------------------------------------------


users=[]

def addusers():
    user={}
    user["reg_no"]=int(input("enter reg no:"))
    reg_nos=[]
    for user in users:
        reg_nos.append(user["reg_no"])

    if user["reg_no"]in reg_nos:
     print("reg no already exists ")
    print("")
    return
    

    user["name"]=input("Enter name:")
    user["subjects"]={}

    subjects=["sql","python","react","java","excel"]
    for subject in subjects:
        marks = int(input(f"Enter {subject} marks:"))
        user["subjects"][subject]=marks

    users.append(user)

def displayusers():
    print(users)
    #     for user in users:
    #         print("----user details----")
    #         print("reg no :",
    # user["reg_no"])
    #         print("name:",user["name"])
    #         print("-------------------")


while True:
    print("----menus----")
    print("1.add users")
    print("2.display users")

    choice=int(input("enter the choice:"))

    if choice==1:
        addusers()
    elif choice==2:
        displayusers()
    else:
        ("Invalid choice")





