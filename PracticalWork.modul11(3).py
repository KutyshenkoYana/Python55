# # Завдання 1
# # Створіть наступні класи:
# #  Rectangle – атрибути width, height
# #  Circle – атрибути radius
# #  Triangle – атрибути a, b, c
# # Методи:
# #  get_perimeter()
# #  display_info()
# # Напишіть функцію create_figure() яка запитує у користувача
# # тип фігури та потрібні атрибути і повертає об’єкт.
# # Створіть декілька фігур, добавте їх у список та для кожної
# # викличте відповідні методи.
#
# import math
#
# class Rectangle:
#     def __init__(self, width: float, height: float):
#         self._width = width
#         self._height = height
#
#
#     def get_perimeter(self) -> float:
#         return (self._width + self._height) * 2
#
#
#     def display_info(self):
#         print(f"Width: {self._width}, Height: {self._height}")
#
#
# class Circle:
#     def __init__(self, radius:float):
#         self._radius = radius
#
#
#     def get_perimeter(self) -> float:
#         return 2 * math.pi * self._radius
#
#
#     def display_info(self):
#         print(f"Radius: {self._radius}")
#
#
# class Triangle:
#     def __init__(self, a:float, b:float, c:float):
#         self._a = a
#         self._b = b
#         self._c = c
#
#
#     def get_perimeter(self) -> float:
#         return self._a + self._b + self._c
#
#
#     def display_info(self):
#         print(f"A: {self._a}, B: {self._b}, C: {self._c}")
#
#
# def create_figure() -> Rectangle | Circle | Triangle | None:
#     figure_type = input("Enter figure type (Rectangle, Circle, Triangle): ")
#
#     if figure_type == "Rectangle":
#         width = float(input("Enter width: "))
#         height = float(input("Enter height: "))
#
#         return Rectangle(width, height)
#
#     elif figure_type == "Circle":
#         radius = float(input("Enter radius: "))
#
#         return Circle(radius)
#
#     elif figure_type == "Triangle":
#         a = float(input("Enter a: "))
#         b = float(input("Enter b: "))
#         c = float(input("Enter c: "))
#
#         return Triangle(a, b, c)
#
#     else:
#         print("Invalid figure type")
#         return None
#
#
# figure = []
#
# for _ in range(3):
#     figur = create_figure()
#
#     if figur is not None:
#         figure.append(figur)
#
# for figur in figure:
#     figur.display_info()
#     print(f"Perimeter: {figur.get_perimeter()}")
#
#
# # Завдання 2
# # Створіть наступні класи:
# #  Manager – атрибути name, base_salary
# #  Developer – атрибути name, base_salary, work_experience
# #  Inter – атрибути name, base_salary
# # Методи:
# #  get_salary() – менеджер отримує базову ставку,
# # Практичне завдання
# # розробник отримує на 20% більше якщо стаж більше 4
# # років, інтерн отримує половину базової ставки
# # Напишіть функцію create_worker() яка запитує у
# # користувача тип працівника та потрібні атрибути і повертає
# # об’єкт.
# # Створіть декілька співробітників, добавте їх у список та для
# # кожного викличте відповідні методи.
#
# class Manager:
#     def __init__(self, name:str, base_salary:float):
#         self._name = name
#         self._base_salary = base_salary
#
#
#     def get_salary(self) -> float:
#         return self._base_salary
# #
# #
# class Developer:
#     def __init__(self, name:str, base_salary:float, work_experience:float):
#         self._name = name
#         self._base_salary = base_salary
#         self._work_experience = work_experience
#
#
#     def get_salary(self) -> float:
#         if self._work_experience > 4:
#             return self._base_salary * 1.2
#
#         else:
#             return self._base_salary
#
#
# class Inter:
#     def __init__(self, name:str, base_salary:float):
#         self._name = name
#         self._base_salary = base_salary
#
#
#     def get_salary(self) -> float:
#         return self._base_salary * 0.5
#
#
# def create_worker() -> Manager | Developer | Inter | None:
#     worker_type = input("Enter worker type (Manager, Developer, Inter): ")
#
#     if worker_type == "Manager":
#         name = input("Enter worker name: ")
#         base_salary = float(input("Enter base salary: "))
#
#         return Manager(name, base_salary)
#
#     elif worker_type == "Developer":
#         name = input("Enter worker name: ")
#         base_salary = float(input("Enter base salary: "))
#         work_experience = float(input("Enter work experience: "))
#
#         return Developer(name, base_salary, work_experience)
#
#     elif worker_type == "Inter":
#         name = input("Enter worker name: ")
#         base_salary = float(input("Enter base salary: "))
#
#         return Inter(name, base_salary)
#
#     else:
#         print("Invalid worker type")
#         return None
#
#
# workers = []
#
# for _ in range(3):
#     worker = create_worker()
#
#     if worker is not None:
#         workers.append(worker)
#
# for worker in workers:
#     print(f"Name: {worker._name}, Salary: {worker.get_salary()}")
#
#
# # Завдання 3
# # Створіть наступні класи:
# #  Car – атрибути speed
# #  Bicycle – атрибути speed
# #  Boat – атрибути speed
# # Методи:
# #  move() – виводить повідомлення про рух
# # o Car – їде по шосе зі швидкістю
# # o Bicycle – їде по дорозі зі швидкістю
# # o Boat – пливе по воді зі швидкістю
# #  check_speed(speed) – перевіряє чи правильна швидкість,
# # якщо ні то в __init__ треба викикати ValueError з
# # відповідним повідомленням
# # o Car – від 20 до 200
# # o Bicycle – від 10 до 30
# # o Boat – від 0 до 50
# # Напишіть функцію create_vehicle() яка запитує у
# # користувача тип транспорту та потрібні атрибути і повертає
# # об’єкт.
# # Створіть декілька транспортних засобів, добавте їх у список
# # та для кожної викличте відповідні методи.
#
# class Car:
#     def __init__(self, speed: float):
#         self.check_speed(speed)
#         self._speed = speed
#
#
#     def move(self):
#         print(f"Car is driving on the highway at {self._speed} km/h")
#
#
#     def check_speed(self, speed) -> float:
#         if speed < 20 or speed > 200:
#             raise ValueError("Car speed must be between 20 and 200")
#
#
# class Bicycle:
#     def __init__(self, speed: float):
#         self.check_speed(speed)
#         self._speed = speed
#
#
#     def move(self):
#         print(f"Bicycle is riding on the road at {self._speed} km/h")
#
#
#     def check_speed(self, speed) -> float:
#         if speed < 10 or speed > 30:
#             raise ValueError("Bicycle speed must be between 10 and 30")
#
#
# class Boat:
#     def __init__(self, speed: float):
#         self.check_speed(speed)
#         self._speed = speed
#
#
#     def move(self):
#         print(f"Boat is sailing on water at {self._speed} km/h")
#
#
#     def check_speed(self, speed) -> float:
#         if speed < 0 or speed > 50:
#             raise ValueError("Boat speed must be between 0 and 50")
#
#
# def create_vehicle() -> Car | Bicycle | Boat | None:
#     vehicle_type = input("Please enter your vehicle type (Car, Bicycle, Boat): ")
#
#     try:
#         speed = float(input("Please enter your vehicle speed: "))
#
#         if vehicle_type == "Car":
#             return Car(speed)
#
#         elif vehicle_type == "Bicycle":
#             return Bicycle(speed)
#
#         elif vehicle_type == "Boat":
#             return Boat(speed)
#
#         else:
#             print("Invalid vehicle type")
#             return None
#
#     except ValueError as e:
#         print(f"Error: {e}")
#         return None
#
#
# vehicles = []
#
# for _ in range(3):
#     vehicl = create_vehicle()
#
#     if vehicl is not None:
#         vehicles.append(vehicl)
#
# for vehicle in vehicles:
#     vehicle.move()
