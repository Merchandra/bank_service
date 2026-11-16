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