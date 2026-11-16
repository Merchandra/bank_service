# 1.Multiply Corresponding Numbers

# numbers1 = [10, 20, 30]
# numbers2 = [2, 3, 4]
# # output: 20 60 120

# for a,b in zip(numbers1,numbers2):
#     print(a*b)


# 2.Compare Corresponding Values
# numbers1 = [10, 50, 30]
# numbers2 = [20, 40, 30]
# output:
# 20 is larger
# 50 is larger
# Both are equal


# numbers1 = [10, 50, 30]
# numbers2 = [20, 40, 30]

# for a,b in zip(numbers1,numbers2):
#     if a > b:
#         print(a,"is larger")
#     elif b > a:
#         print(b,"is largest")
#     else:
#         print ("Both are equal")



# 3.Count Pairs Whose Sum Is Even
# numbers1 = [10, 15, 20, 25]
# numbers2 = [2, 3, 5, 7]

# count=0

# for a,b in zip(numbers1,numbers2):
#     if(a+b)% 2 == 0:
#         count+=1
# print(count)







# 4.Create a List of Pair Products
# numbers1 = [10, 20, 30]
# numbers2 = [2, 3, 4]


# for a,b in zip(numbers1,numbers2):
#     result.append(a*b)
# print(result)




# # 4.Pair IDs Generated with Names
# names = ["Ram", "Sam", "Arun", "Ravi"]
# # Output
# # [
# #     (101, 'Ram'),
# #     (102, 'Sam'),
# #     (103, 'Ajay'),
# #     (104, 'Ravi')
# # ]

# for user in zip (range(101,105),names):
#         print(user)



# 5.Calculate Total Price from Product, Price, and Quantity
# products = ["Laptop", "Mouse", "Keyboard"]
# prices = [50000, 500, 1500]
# quantities = [2, 3, 4]



# for product,price,quantity in zip(products,prices,quantities):
#     total=price*quantity
#     print(product,total)
                                



# 6.Print Available Products Using Stock
# products = ["Laptop", "Mouse", "Keyboard"]
# prices = [50000, 500, 1500]
# stocks = [10, 0, 5]


# for product,price,stock in zip(products,prices,stocks):
#     if stock > 0:
#         print(product,price,stock)





# 7.Create Dictionaries from Three Related Lists as Nested Values
# names = ["Ram", "Sam", "Arun"]
# marks = [80, 70, 95]
# grades = ["A", "B", "A+"]

# student={}
# for name,mark,grade in zip (names,marks,grades):
#     student[name]={"marks":mark,"grade":grade}
#     print(student)



# 8.Separate Products and Prices
# data = [
#     ("Laptop", 50000),
#     ("Mouse", 500),
#     ("Keyboard", 1500)
# ]
# # Output:
# # ('Laptop', 'Mouse', 'Keyboard')
# # (50000, 500, 1500)


# products,prices=zip(*data)
# print(products)
# print(prices)



# 9.Convert Unzipped Tuples Back to Lists
# data = [
#     ("Ram", 80),
#     ("Sam", 70),
#     ("Arun", 95)
# ]

# names,marks = zip(*data)

# names=list(names)
# marks=list(marks)

# print(names)
# print(marks)





# 10.Transport — Match Bus Numbers with Routes
# bus_numbers = ["21G", "27D", "70"]
# routes = [
#     "Tambaram - Broadway",
#     "Anna Nagar - T Nagar",
#     "Guindy - Avadi"
# ]

# for bus ,route in zip (bus_numbers,routes):

#  print(bus,":",routes)





# 1.Booking System — Check Whether Any Booking Is Cancelled
# statuses = [
#     "Confirmed",
#     "Completed",
#     "Cancelled",
#     "Confirmed"
# ]

# result=any(status == "Cancelled" for status in statuses)
# print(result)



# 2.Food Delivery — Check Whether Any Order Is Delayed
# orders = [
#     {"id": 101, "status": "Delivered"},
#     {"id": 102, "status": "Delayed"},
#     {"id": 103, "status": "Preparing"}
# ]

# result=any(order["status"]=="Delayed" for order in orders)
# print(result)




# 3.Check Whether Any Matrix Row Contains Zero
# matrix = [
#     [1, 2, 3],
#     [4, 0, 6],
#     [7, 8, 9]
# ]

# result=any(0 in row for row in matrix)
# print(result)



# 4.Booking System — Check Whether All Selected Slots Are Available

# slots = [
#     "Available",
#     "Available",
#     "Available"
# ]

# result=all(slot == "Available" for slot in slots)
# print(result)

# 5.Data Validation — Check Whether All Ages Are Valid
# Suppose valid age is: 0 to 120

# ages=[20,35,60,18]
# result = all( 0 <=age <=120 for age in ages)
# print(result)


# 6.Security System — Check Whether All Security Checks Passed

# security_checks = [
#     True,
#     True,
#     True,
#     True
# ]
# result =all(security_checks)
# print(result)


# 1.Find Pairs Whose Sum Equals a Target
# numbers1 = [10, 20, 30, 40]
# numbers2 = [5, 10, 20, 15]
# target = 50
# # Output:
# # 30 20

# for a,b in zip(numbers1,numbers2):
#     if a+b == target:
#         print(a,b)




# 2.Build an Adjacency Mapping from Source and Destination Arrays
sources = ["A", "A", "B", "C"]
destinations = ["B", "C", "D", "D"]
# Output:
# {
#     'A': ['B', 'C'],
#     'B': ['D'],
#     'C': ['D']
# }


# result={}

# for source , destination in zip(sources,destinations):
#     if source not in result:
#         result[source]=[]
#     result[source].append(destination)

# print(result)



# 3.Find a Pair with a Target Sum and Return Indexes
# numbers = [2, 7, 11, 15]
# target = 9

# seen={}

# for index,number in enumerate (numbers):
#     remaining=target-number
#     if remaining in seen:
#         print(seen[remaining],index)
#         break
#     seen[number]=index






# 4.Find the Distance Between Repeated Occurrences
# numbers = [10, 20, 30, 20, 40]
# Output
# Value: 20
# Distance: 2

# numbers=[10,20,30,20,40]
# positions={}

# for index ,number in enumerate (numbers):
#     if number in positions:
#         distance=index-positions[number]  
#         print("value:",number)
#         print("Distance:",distance)
#         break
#     else:
#         positions[numbers]=index
#                                                 index 1=20
#                                                 index 3=20
#                                                 distance=3-1=2


# 5.Find the Longest Run's Starting Position
# A run means consecutive equal values.
# Example: 10, 20, 20, 20, 30, 30
# The longest run is: 20, 20, 20
# Starting index: 1
# Output:
# Start Index: 1
# Length: 3


# numbers=[10,20,20,20,30,30]
# max_lengh=1
# current_length=1
# max_stare=0

# for i in range(1,len(numbers)):
#     if numbers[i]== numbers[i-1]:
#         current_length+=1
#     else:
#         current_length=1
#         start_index=i

#     if current_length>max_lengh:
#         max_lengh=current_length
#         max_start=start_index 

# print("Start Index:",max_start)
# print("Length:",max_lengh)



# 6.Check Whether All Adjacent Values Are Different
# numbers = [10, 20, 30, 20, 40]

# result=all(numbers[i] != numbers[i+1]
#            for i in range(len (numbers)-1))
# print(result)


# 7.Check Whether Every Matrix Row Contains a Target
# matrix = [
#     [1, 2, 3],
#     [4, 2, 6],
#     [7, 2, 9]
# ]
# target = 2


# result=all(target in row for row in matrix)
# print(result)






# 8.Check Whether Every Dictionary Frequency Is Below k
# frequency = {
#     "a": 2,
#     "b": 1,
#     "c": 3
# }
# k = 4

# result=all(value < k for value in frequency.values())
# print(result)