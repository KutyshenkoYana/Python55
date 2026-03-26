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
