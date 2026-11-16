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



