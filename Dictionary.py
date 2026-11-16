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

