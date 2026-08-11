# Task 1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a * b)


# Task 2
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

print((a + b + c) / 3)


# Task 3
length = float(input("Enter length: "))
width = float(input("Enter width: "))

print(length * width)


# Task 4
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

print(a + b + c)


# Task 5
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius * 9 / 5 + 32

print(fahrenheit)


# Task 6
minutes = int(input("Enter number of minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print(f"{hours} hours {remaining_minutes} minutes")


# Task 7
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a % b)


# Task 8
n = int(input("Enter an integer: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# Task 9
n = int(input("Enter an integer: "))

if n % 3 == 0 and n % 5 == 0:
    print("The number is divisible by 3 and 5")
else:
    print("The number is not divisible by 3 and 5")


# Task 10
price = float(input("Enter the original price: "))
discount = float(input("Enter the discount percentage: "))

final_price = price * (1 - discount / 100)

print(final_price)


# Task 11
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("First number is greater")
elif b > a:
    print("Second number is greater")
else:
    print("The numbers are equal")


# Task 12
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


# Task 13
n = float(input("Enter a number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")


# Task 14
score = int(input("Enter score from 0 to 100: "))

if 90 <= score <= 100:
    print("12 points")
elif 75 <= score <= 89:
    print("9-11 points")
elif 60 <= score <= 74:
    print("6-8 points")
elif score < 60:
    print("Unsatisfactory")
else:
    print("Invalid score")


# Task 15
year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")


# Task 16
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("Triangle exists")
else:
    print("Triangle does not exist")


# Task 17
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or a == c or b == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


# Task 18
correct_password = "12345"

password = input("Enter password: ")

if password == correct_password:
    print("Correct password")
else:
    print("Incorrect password")


# Task 19
correct_login = "admin"
correct_password = "12345"

login = input("Enter login: ")
password = input("Enter password: ")

if login == correct_login and password == correct_password:
    print("Login successful")
else:
    print("Error")


# Task 20
month = int(input("Enter month number (1-12): "))

if month in (12, 1, 2):
    print("Winter")
elif month in (3, 4, 5):
    print("Spring")
elif month in (6, 7, 8):
    print("Summer")
elif month in (9, 10, 11):
    print("Autumn")
else:
    print("Invalid month")