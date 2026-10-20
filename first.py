# print("hello world")

# name="dev"
# age=17
# print(name)
# print(age)

# n=int(input("enter a number:"))
# if n%2==0:
#     print("even")
# else:
#     print("odd")

# n=int(input("enter a number:"))
# if n>0:
#     print("positive")
# elif n<0:
#     print("negative")
# else:
#     print("zero")

# n=int(input("enter a number:"))
# if n>=10:
#     print("greater than or equal to 10")
# else:
#     print("less than 10")

# a=15
# b=25
# c=45
# if a>b and a>c:
#     print("a is greater")
# elif b>c and b>a:
#     print("b is greater")
# else:
#     print("c is greater")

# n=int(input("enter a number:"))
# total=0
# for i in range(1,n+1):
#     total=total+i
# print("sum of first",n,"numbers is:",total)

# def find_even_numbers(n):
#     even_numbers=[]
#     for i in range(1,11):
#         if i%2==0:
#             even_numbers.append(i)
#     return even_numbers
# find_even_numbers(10)
# print(find_even_numbers(10))

# n=int(input("enter a number:"))
# for i in range(1,11):
#     multiply=i*n
#     print("5 X",i,"=",multiply)
        
# n=int(input("enter a number:"))
# if n<=0:
#     print("not a prime number")
# else:
#     is_prime=True
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print(n,"is a prime number")
#     else:
#         print(n,"is not a prime number")

# n=int(input("enter a number:"))
# result=1
# for i in range(1,n+1):
#     result=result*i
# print(result)

# n=int(input("enter a number:"))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c

# n="python"
# print(n[::-1])

# n=input("enter a word:")
# if n==n[::-1]:
#     print(n,"is a palindrome")
# else:
#     print(n,"is not a palindrome")

# def count_vowels(s):
#     vowels="aeiouAEIOU"
#     count=0
#     for char in s:
#         if char in vowels:
#            count=count+1
#     return count
# s="i love python"
# print("number of vowels in the string:",count_vowels(s))

# def count_words(s):
#     words=s.split()
#     return len(words)
# print(count_words("i love python"))

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# n=int(input("enter a number of terms:"))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c

# student={
#     "name":"arun",
#     "marks":78
#     }
# print(student["name"])
# print(student["marks"])
# if student["marks"]>=60:
#     print("pass")
# else:
#     print("fail")

# prices={
#     "pen":10,
#     "book":50,
#     "bag":500
# }
# total=0
# for item in prices:
#     total=total+prices[item]
# print("total price:",total)

# def area_rectangle(length,width):
#     return length*width
# area=area_rectangle(5,10)
# print("area of rectangle:",area)

# s=" hello world "
# print(s.upper())
# print(s.lower())
# print(s.replace("world","python"))
# print(s.strip())
# print(s.split())

# def student(name,roll_no,marks):
#     print("name:",name)
#     print("roll_no:",roll_no)
#     print("marks:",marks)
# name="arun"
# roll_no=101
# marks=78
# student(name,roll_no,marks)

