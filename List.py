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

