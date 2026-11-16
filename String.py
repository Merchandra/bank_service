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