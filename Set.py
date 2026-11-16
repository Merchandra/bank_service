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