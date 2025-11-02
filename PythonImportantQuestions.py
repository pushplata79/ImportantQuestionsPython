#Write a program to find average of ‘n’ natural numbers
# n=10
# s=0
# for i in range(1,n+1):
#   s=s+i
# av=s/n   #calculating average
# print("average of",n,"is",av)

# Write a program to print the pattern
# *
# * *
# * * *
# * * * *

# n=int(input("enter the rows")) 
# for i in range(1,n+1):
#   print("*"*i)  



# Write a program to find factorial of a given number.

# n=6  
# f=1
# p=n
# while(n>0):
#   f=f*n
#   n=n-1
# print("factorial of ",p,"is",f)

# Write a program to display ‘n’ numbers of Fibonacci Series.
# n=int(input("enter number of terms"))
# a,b=0,1
# c=0
# print("fabonacci series")
# for i in range(n):  #8
#   print(c)  
#   c=a+b
#   b=a
#   a=c
  


# Write a program to display nth number of Fibonacci Series.

# n=int(input("enter number n"))
# a,b=0,1
# c=0
# while c<=n:
#   print(c)  
#   c=a+b
#   b=a
#   a=c

#Write a program to find list of prime numbers in the given range using functions

# def is_prime(n):
#   if n<2:
#     return False
#   for i in range(2,n):
#     if n%i==0:
#       return False
#   return True


# s=int(input("enter the start value")) 

# e=int(input("enter the end value"))

# for i in range(s,e+1):
#   if is_prime(i): 
#      print(i,end="") 

# Write a program to sort the given list of array using bubble sort.

# 8 9 3 2 1 99 56 4 30   unsorted

# 8 3 2 1 9 56 4 30 99 pass1 i=0 j=0,1,2,3,4,5,6,7

# 3 2 1 8 9 4 30 56 99 pass 2 i=1 j=0,1,2,3,4,5,6,7

# 2 1 3 8 4 9 30 56 99 pass 3 i=2 j=0,1,2,3,4,5,6,7

# 1 2 3 4 8 9 30 56 99 pass 4 i=3 j=0,1,2,3,4,5,6,7

# 1 2 3 4 8 9 30 56 99 pass 5 i=3 j=0,1,2,3,4,5,6,7
# 1 2 3 4 8 9 30 56 99 pass 6 i=3 j=0,1,2,3,4,5,6,7

# arr=[8,9,3,2,1,99,88,30]
# print("unsorted array",arr)
# n=len(arr)
# for i in range(0,n-1):
#   for j in range(0,n-1):
#      if(arr[j]>arr[j+1]):
#         arr[j],arr[j+1]=arr[j+1],arr[j]
# print("sorted array is",arr)



# Write a program to accepts a word from the user and reverse it.

# w="sam" #string collection of characters
# print("reverse word is",w[::-1]) 


# Write a program to calculate number of Uppercase and Lowercase letter from string.
# s=input("enter the text")
# u=sum(1 for ch in s if ch.isupper())
# l=sum(1 for ch in s if ch.islower())
# print("uppercase letters",u)
# print("lowercase letters",l)
      

# Write a program to extract substring from given string.
# str=input("enter the text")
# s=int(input("enter starting index"))
# e=int(input("enter end index"))
# print("substring",str[s:e])



# Write a program to create and print a list where values are square between 1 to 10

# sq=[i**2 for i in range(1,11)]
# print(sq)
# # Write a program to check number is Armstrong or not
 
# n=234
# s=0
# p=n
# while n>0:
#   r=n%10
#   s=s+(r*r*r)
#   n=n//10
# if p==s:
#   print("armstrong")
# else:
#   print("not")


# Write a program to count the frequency of words in a file.

f=input("enter the file name")
with open(f,"r") as file:
  t=file.read().split()
freq={}
for word in t:
  freq[word]=freq.get(word,0)+1
print(freq)

# Write a program to sum all the items in a dictionary

d = {'a': 10, 'b': 20, 'c': 30}
print("Sum of all items:", sum(d.values()))

# Write a program to add two matrices using tuple and display.
A = ((1, 2, 3), (4, 5, 6))
B = ((7, 8, 9), (1, 2, 3))

result = tuple(tuple(A[i][j] + B[i][j] for j in range(len(A[0]))) for i in range(len(A)))
print("Sum of matrices:", result)


# Write a program to multiply two matrices and display resltauant matrices.
# A = [[1, 2], [3, 4]]
# B = [[2, 0], [1, 2]]

# result = [[0, 0], [0, 0]]
# for i in range(len(A)):
#     for j in range(len(B[0])):
#         for k in range(len(B)):
#             result[i][j] += A[i][k] * B[k][j]

# print("Resultant Matrix:")
# for row in result:
#     print(row)

# Write a program to convert month name to a number of days.
# Expected Output:
# List of months: January,February,March,April,May,June,July,August,September,October,November,December.
# Input the Name of Month:March
# Number of Days:31 days

month_days = {
    "January": 31, "February": 28, "March": 31, "April": 30,
    "May": 31, "June": 30, "July": 31, "August": 31,
    "September": 30, "October": 31, "November": 30, "December": 31
}

month = input("Input the Name of Month: ")
print("Number of Days:", month_days.get(month, "Invalid month"), "days")



# Write a program script to concatenate following dictionaries to create a new one.
# Sample Dictionary
# Dic1={1:10,2:20}
# Dic2={3:30,4:40}
# Dic3={5:50,6:60}
# Expected Result:
# {1:10,2:20,3:30
# 4:40,5:50,6:60}

Dic1 = {1: 10, 2: 20}
Dic2 = {3: 30, 4: 40}
Dic3 = {5: 50, 6: 60}
result = {}
for d in (Dic1, Dic2, Dic3):
    result.update(d)
print(result)



# Write a program to generate sum of following series
# 1 + x + x2 + x3 + x4 + x5. . . . .+xn


x = int(input("Enter value of x: "))
n = int(input("Enter value of n: "))
total = sum(x**i for i in range(n + 1))
print("Sum of series:", total)


# Write a program to create a list of seven colors of VIBGYOR and iterate over a list.
colors = ["Violet", "Indigo", "Blue", "Green", "Yellow", "Orange", "Red"]
for color in colors:
    print(color)




# Write a program to find the maximum and minimum in a list.

lst = [12, 45, 7, 89, 34]
print("Maximum:", max(lst))
print("Minimum:", min(lst))



# Write a program to find whether is palindrome or not.

s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# Write a program that inputs the elements of a dictionary containing student roll number and its name using for loop and then display it.

n = int(input("Enter number of students: "))
students = {}
for i in range(n):
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    students[roll] = name

print("Student Dictionary:", students)





# Write a program using conditional statements to find out discounted price for an item depending upon its category such as
# I. seasonal-food-items with expiry date in a month at 10% and otherwise 5%
# II.seasonal clothes with sizes extra-small, or extra-extra-large at 20% and otherwise 5%.




category = input("Enter category (food/clothes): ").lower()
price = float(input("Enter price: "))

if category == "food":
    expiry = input("Expiry within a month? (yes/no): ").lower()
    discount = 10 if expiry == "yes" else 5
elif category == "clothes":
    size = input("Enter size (XS, S, M, L, XL, XXL): ").lower()
    discount = 20 if size in ["xs", "xxl"] else 5
else:
    discount = 0

discounted_price = price - (price * discount / 100)
print(f"Discounted Price: {discounted_price}")


# Write down a program to check condition of room allotment in a hotel. Rooms at the ground floor are in luxury category and are costlier than the rooms at first and second floors. The hotel has no list facility. Write logic to allocate rooms to able/differently abled visitors as per their budget preference. Print message’ Room not available’ if there is no room as per visitor’s requirements.

budget = input("Enter budget preference (high/medium/low): ").lower()
ability = input("Is visitor differently abled? (yes/no): ").lower()

if ability == "yes":
    floor = "Ground Floor (Luxury)" if budget == "high" else "First Floor"
elif ability == "no":
    floor = "Any floor" if budget in ["medium", "high"] else "Second Floor"
else:
    floor = "Room not available"

print("Room allocation:", floor)



# Write a python program that accepts a word from user and reverse it.

word = input("Enter a word: ")
print("Reversed word:", word[::-1])



# Write a python program to count the number of words, characters, digits, special characters, vowels and consonants in a string.

text = input("Enter a string: ")
words = text.split()
vowels = "aeiouAEIOU"
v = c = d = s = 0
for ch in text:
    if ch.isdigit():
        d += 1
    elif ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1
    else:
        s += 1
print("Words:", len(words))
print("Characters:", len(text))
print("Digits:", d)
print("Special characters:", s)
print("Vowels:", v)
print("Consonants:", c)


# Write a python program to write contents to a file using writelines().

lines = ["Hello\n", "Welcome to Python\n", "File Handling Example\n"]
with open("sample.txt", "w") as f:
    f.writelines(lines)
print("File written successfully!")



# Write a python program to write contents to a file using write().

text = "This is a single line written using write()."
with open("sample2.txt", "w") as f:
    f.write(text)
print("File written successfully!")



# Write a python program to append contents to a file.
text = "\nThis line is appended to the file."
with open("sample2.txt", "a") as f:
    f.write(text)
print("File appended successfully!")


# Write a python program to read contents of existing file using readline().

with open("sample.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()



# Write a python program to read contents of existing file using read().
with open("sample.txt", "r") as f:
    content = f.read()
print("File contents:\n", content)



# Write a python program that handles multiple exceptions.
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ValueError:
    print("Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division result:", result)
finally:
    print("Execution completed.")


# Write a python program that handles exception and use else and finally clause in one program.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ValueError:
    print("Error: Please enter valid numbers only.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print("Division successful! Result =", result)
finally:
    print("Program execution completed.")
