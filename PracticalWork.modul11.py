# Завдання 1
# Створіть клас Student з атрибутами name та age. Додайте
# метод для виводу інформації у форматі «Ім’я: {name}, вік:
# {age}»

# class Student:
#     def __init__(self, name, age):
#         self.name = name.capitalize()
#         self.age = age
#
#     def check_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
#
# student1 = Student("Yana", 19)
#
# student1.check_info()

# Завдання 2
# Створіть список з 3-ма студентами, дані вводить
# користувач. Після чого для кожного студента виведіть
# інформацію про нього за допомогою метода.

# class Student:
#     def __init__(self, name, age):
#         self.name = name.capitalize()
#         self.age = age
#
#     def check_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#
#
# students = []
#
# for i in range(3):
#     name = input("Enter student name: ").capitalize()
#     age = input("Enter student age: ")
#
#     student = Student(name, age)
#     students.append(student)
#
# for student in students:
#     student.check_info()

# Завдання 3
# Створіть клас Circle з атрибутом radius. Додайте метод для
# отримання площі кола

# import math
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#       return math.pi * self.radius ** 2
#
#
# radius_area = Circle(10)
#
# print(radius_area.get_area())

# Завдання 4
# Створіть клас BankAccount з атрибутами owner та balance.
# Додайте метод deposit для поповнення рахунку
# Додайте метод withdraw для зняття грошей з рахунку
# Додайте метод info для виведення інформації про баланс

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner.capitalize()
#         self.balance = balance
#
#
#     def deposit(self, deposit_amount):
#         self.balance += deposit_amount
#
#
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#
#         else:
#             print("You don't have enough money to withdraw")
#
#
#     def info(self):
#         print(f"{self.owner}'s balance is {self.balance}")
#

# owner1 = BankAccount("Yana", 10000)
#
# owner1.deposit(1000)
# owner1.withdraw(10000)
# owner1.info()

# Завдання 5
# Створіть клас Car з атрибутами brand(марка), year(рік
# випуску), is_ready(чи готовий до поїздки, за замовчування
# False).
# Додайте метод start_engine який заводить двигун, і змінює
# атрибут is_ready
# Додайте метод move який виводить повідомлення, що
# автомобіль їде, або ж ще не готовий в залежності від is_ready.


class Car:
    def __init__(self, brand, year, is_ready=False):
        self.brand = brand
        self.year = year
        self.is_ready = is_ready

    def start_engine(self):
        self.is_ready = True

    def move(self):
        if self.is_ready is True:
            print("Car is moving")

        else:
            print("Car is not moving")


car1 = Car("Ford", 2010, False)
car1.start_engine()
car1.move()
