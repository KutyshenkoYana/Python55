# Завдання 1
# Створіть клас Проект з атрибутами:
#  назва
#  виділений кошторис
#  загальні витрати
#  чи завершений(за замовчуванням False)
#  час виконання(за замовчуванням 0 місяців)
#  список необхідних задач
# Додайте методи:
#  вивід інформації: назва, час виконання, необхідні
# задачі
#  добавити нову задачу
#  розбити задачу на під-задачі: передається назва задачі
# та список під-задач
#  виконати задачу, передається назва, час та ціна
# виконання
#  поповнення кошторису

import random


class Project:
    def __init__(self, name, budget):
        self._name = name
        self._budget = budget
        self._total_costs = 0
        self._is_completed = False
        self._execution_time = 0
        self._tasks = []

    def show_info(self):
        print(f"Project: {self._name}")
        print(f"Execution time: {self._execution_time} months")
        print(f"Tasks: {self._tasks}")

    def add_task(self, task_name):
        self._tasks.append(task_name)

    def split_task(self, task_name, subtasks):
        if task_name in self._tasks:
            self._tasks.remove(task_name)
            self._tasks.extend(subtasks)

    def complete_task(self, task_name, time, cost):
        if task_name in self._tasks:
            self._tasks.remove(task_name)
            self._execution_time += time
            self._total_costs += cost

            if self._total_costs > self._budget:
                print("Budget exceeded!")

            if len(self._tasks) == 0:
                self._is_completed = True

    def add_budget(self, amount):
        self._budget += amount


project = Project("Website", 5000)

project.add_task("Design")
project.add_task("Backend")

project.show_info()

project.split_task("Backend", ["API", "Database"])

project.complete_task("Design", 1, 1000)

project.add_budget(2000)


# Завдання 2
# Створіть клас Телефон з атрибутами:
#  максимальний обсяг пам’яті
# Практичне завдання
#  зайнята пам’ять
#  чи включений(за замовчуванням False)
#  встановлені додатки у вигляді словника, де ключ –
# назва додатку, значення – обсяг пам’яті
# Додайте методи:
#  вивести інформацію про використання пам’яті
#  видалити додаток
#  встановити новий додаток, якщо пам’яті достатньо
#  оновити додаток(нова версія може займати іншу
# кількість пам’яті)
#  запустити додаток, якщо він є і якщо телефон
# вкючений
#  включити телефон
#  виключити телефон


class Phone:
    def __init__(self, max_memory):
        self._max_memory = max_memory
        self._used_memory = 0
        self._is_on = False
        self._apps = {}

    def show_memory_info(self):
        print(f"Used memory: {self._used_memory}/{self._max_memory} GB")

    def delete_app(self, app_name):
        if app_name in self._apps:
            self._used_memory -= self._apps[app_name]
            del self._apps[app_name]

    def install_app(self, app_name, memory):
        if self._used_memory + memory <= self._max_memory:
            self._apps[app_name] = memory
            self._used_memory += memory
            print(f"{app_name} installed")
        else:
            print("Not enough memory")

    def update_app(self, app_name, new_memory):
        if app_name in self._apps:
            old_memory = self._apps[app_name]
            difference = new_memory - old_memory

            if self._used_memory + difference <= self._max_memory:
                self._apps[app_name] = new_memory
                self._used_memory += difference
                print(f"{app_name} updated")
            else:
                print("Not enough memory for update")

    def run_app(self, app_name):
        if self._is_on and app_name in self._apps:
            print(f"Running {app_name}")
        else:
            print("Cannot run app")

    def turn_on(self):
        self._is_on = True
        print("Phone is ON")

    def turn_off(self):
        self._is_on = False
        print("Phone is OFF")


phone = Phone(128)

phone.turn_on()

phone.install_app("Telegram", 5)
phone.install_app("Instagram", 10)

phone.show_memory_info()

phone.update_app("Telegram", 7)

phone.run_app("Telegram")

phone.delete_app("Instagram")

phone.turn_off()


# Завдання 3
# Створіть клас Автомобіль з атрибутами:
#  марка
#  пробіг
#  рівень пального
#  витрата пального(л/км)
#  чи є справним(за замовчуванням True)
# Реалізуйте методи:
#  проїхати певну відстань, має змінитись пробіг та рівень
# пального, якщо автомобіль справний та достатньо
# пального
# З ймовірністю 40% автомобіль може зламатись
#  ремонт
#  поповнення пального


class Car:
    def __init__(self, brand, fuel_consumption):
        self._brand = brand
        self._mileage = 0
        self._fuel_level = 0
        self._fuel_consumption = fuel_consumption
        self._is_working = True

    def drive(self, distance):
        needed_fuel = distance * self._fuel_consumption

        if not self._is_working:
            print("Car is broken")
            return

        if self._fuel_level < needed_fuel:
            print("Not enough fuel")
            return

        self._mileage += distance
        self._fuel_level -= needed_fuel

        print(f"Car drove {distance} km")

        if random.randint(1, 100) <= 40:
            self._is_working = False
            print("The car broke down!")

    def repair(self):
        self._is_working = True
        print("Car repaired")

    def refuel(self, amount):
        self._fuel_level += amount
        print(f"Added {amount} liters of fuel")


car = Car("BMW", 0.1)

car.refuel(50)

car.drive(100)

car.repair()


# Завдання 4
# Створіть клас Студент з атрибутами:
#  ім’я
#  словник з предметами, де ключ – назва предмету,
# значення – список оцінок
# Додайте методи:
#  додати новий предмет
#  видалити предмет
#  вчити предмет(якщо отримана оцінка, то додати про це
# інформацію)
#  отримати середню оцінку за конкретним предметом
#  вивести загальну інформацію: ім’я та список предметів
# з середніми оцінками


class Student:
    def __init__(self, name):
        self._name = name
        self._subjects = {}

    def add_subject(self, subject_name):
        if subject_name not in self._subjects:
            self._subjects[subject_name] = []

    def remove_subject(self, subject_name):
        if subject_name in self._subjects:
            del self._subjects[subject_name]

    def study_subject(self, subject_name, grade):
        if subject_name in self._subjects:
            self._subjects[subject_name].append(grade)

    def get_average_grade(self, subject_name):
        if subject_name in self._subjects:
            grades = self._subjects[subject_name]

            if len(grades) > 0:
                return sum(grades) / len(grades)

        return 0

    def show_info(self):
        print(f"Student: {self._name}")

        for subject, grades in self._subjects.items():
            average = self.get_average_grade(subject)
            print(f"{subject}: {average}")


student = Student("Anna")

student.add_subject("Math")
student.add_subject("Physics")

student.study_subject("Math", 90)
student.study_subject("Math", 80)

print(student.get_average_grade("Math"))

student.show_info()

student.remove_subject("Physics")


# Завдання 5
# Створіть клас Магазин з атрибутами:
#  назва
#  заробіток
#  словник з товарами, де ключ – назва товару, значення –
# кількість на складі
#  словник з товарами, де ключ – назва товару, значення –
# ціна
# Додайте методи:
#  вивід інформації: назва та список доступних товарів
#  поповнення складу певним товаром(може бути новий)
#  оформлення замовлення, якщо товар у достатній
# кількості доступний


class Shop:
    def __init__(self, name):
        self._name = name
        self._income = 0
        self._products_quantity = {}
        self._products_price = {}

    def show_info(self):
        print(f"Shop: {self._name}")

        for product in self._products_quantity:
            quantity = self._products_quantity[product]
            price = self._products_price[product]

            print(f"{product} - {quantity} pcs - {price}")

    def add_product(self, product_name, quantity, price):
        if product_name in self._products_quantity:
            self._products_quantity[product_name] += quantity
        else:
            self._products_quantity[product_name] = quantity

        self._products_price[product_name] = price

    def make_order(self, product_name, quantity):
        if product_name in self._products_quantity:
            if self._products_quantity[product_name] >= quantity:
                total_price = self._products_price[product_name] * quantity

                self._products_quantity[product_name] -= quantity
                self._income += total_price

                print(f"Order completed. Total price: {total_price}")
            else:
                print("Not enough products in stock")
        else:
            print("Product not found")


shop = Shop("Tech Store")

shop.add_product("Laptop", 10, 1000)
shop.add_product("Mouse", 20, 50)

shop.show_info()

shop.make_order("Laptop", 2)
