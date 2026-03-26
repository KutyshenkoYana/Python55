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


# class Car:
#     def __init__(self, brand, year, is_ready=False):
#         self.brand = brand
#         self.year = year
#         self.is_ready = is_ready
#
#     def start_engine(self):
#         self.is_ready = True
#
#     def move(self):
#         if self.is_ready:
#             print("Car is moving")
#
#         else:
#             print("Car is not moving")
#
#
# car1 = Car("Ford", 2010, False)
# car1.start_engine()
# car1.move()

## Завдання 1 — Клас `BankCard` з лімітами та пін-кодом
# Створіть клас **BankCard** з атрибутами:
#
# *   `owner` — власник картки
# *   `balance` — поточний баланс
# *   `pin` — пін-код
# *   `daily_limit` — денний ліміт зняття грошей
# *   `withdrawn_today` — сума вже знятих за поточний день


class BankCard:
    def __init__(self, owner, balance, pin, daily_limit, withdrawn_today):
        self.owner = owner
        self.balance = balance
        self.pin = pin
        self.daily_limit = daily_limit
        self.withdrawn_today = withdrawn_today

    # **Методи:**
    #
    # 1.  **Метод авторизації по пін-коду**
    #     *   Логіка: перевіряє, чи співпадає введений код з піном картки.
    # Якщо ні — доступ до операцій заборонено.
    #     *   Параметри:
    #         *   `self`
    #         *   `entered_pin` — введений користувачем пін-код

    def check_pin(self, entered_pin):
        if entered_pin == self.pin:
            return True

        else:
            print("Wrong PIN")
            return False

    # 2.  **Метод поповнення рахунку**
    #     *   Логіка: додає суму до балансу, але тільки якщо користувач
    # уже авторизований.
    #     *   Параметри:
    #         *   `self`
    #         *   `amount` — сума поповнення

    def make_deposit(self, amount):
        entered_pin = int(input("Enter PIN to deposit: "))
        if self.check_pin(entered_pin):
            if amount > 0:
                self.balance += amount

            else:
                print("Deposit must be > 0")

        else:
            print("Wrong PIN")


# 3.  **Метод зняття грошей**
#     *   Логіка:
#         *   перевірити, чи авторизований користувач
#         *   перевірити, чи вистачає грошей на балансі
#         *   перевірити, чи не буде перевищено `daily_limit`
#         *   якщо все ок — зменшити баланс і збільшити `withdrawn_today`
#     *   Параметри:
#         *   `self`
#         *   `amount` — сума для зняття

# daily_limit = 20000
#
#     def withdraw_money(self, amount):
#         entered_pin = int(input("Enter PIN to deposit: "))
#
#         if self.check_pin(entered_pin):
#
#             if self.daily_limit < daily_limit:
#
#                 if self.balance >= amount:
#                     self.balance -= amount
#
#                 else:
#                     print("Deposit must be > 0")
#             else:
#                 print("You're reached your daily limit")
#
#         else:
#             print("Wrong PIN")
