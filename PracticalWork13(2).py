# Завдання 1
# Напишіть програму для заповнення списку товарів.
# Назви товарів вводить користувач. Реалізуйте функціонал:
#  додати новий товар
#  вивести список товарів
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle

import json
import pickle


def add_products(items: list[str]) -> None:
    product = input("Enter product name: ")
    items.append(product)
    print(f"{product} added.")


def show_products(items: list[str]) -> None:
    print("Products:")
    for item in items:
        print(item)


def save_products_json(items: list[str], filename: str = "products.json") -> None:
    with open(filename, "w", encoding="utf-8") as f_out:
        json.dump(items, f_out, indent=4, ensure_ascii=False)
        print(f"{filename} saved.")


def save_products_pickle(items: list[str], filename: str = "products.pickle") -> None:
    with open(filename, "wb") as f_out:
        pickle.dump(items, f_out)
        print(f"{filename} saved.")


def load_products_json(filename: str = "products.json") -> list[str]:
    with open(filename, encoding="utf-8") as f_in:
        return json.load(f_in)


def load_products_pickle(filename: str = "products.pickle") -> list[str]:
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


# products = []
#
# add_products(products)
# add_products(products)
#
# save_products_json(products)
# save_products_pickle(products)
#
# load_products_json(filename="products.json")
# load_products_pickle(filename="products.pickle")


# Завдання 2
# Напишіть клас Student
# Атрибути:
#  name – ім’я
#  specialization – спеціалізація
#  grades – список оцінок
# Методи:
#  add_grade(grade) – додати нову оцінку
#  show_info() – вивести ім’я, спеціалізацію та середню
# оцінку
# Практичне завдання
# Створіть список з трьох студентів. Збережіть цей список
# використовуючи pickle та json.
# Завантажте дані за допомогою pickle та json.


class Student:
    def __init__(
        self,
        name: str,
        specialization: str,
        grades: list[int],
    ):
        self._name = name
        self._specialization = specialization
        self._grades = grades

    def add_grade(
        self,
        grade: int,
    ):
        self._grades.append(grade)
        print(f"{grade} added.")

    def show_info(self):
        print(f"Name: {self._name}.")
        print(f"Specialization: {self._specialization}.")
        print(f"Average grade: {self._average_grade()}")

    def _average_grade(self):
        if len(self._grades) == 0:
            return None

        average = sum(self._grades) / len(self._grades)
        return average

    def save_json(
        self,
        filename: str = "student.json",
    ):
        with open(filename, "w", encoding="utf-8") as f_out:
            json.dump(self._get_state_dict(), f_out, indent=4)

    def _get_state_dict(self):
        return {
            "Name": self._name,
            "Specialization": self._specialization,
            "Grades": self._grades,
        }

    def _set_state_dict(
        self,
        state_dict: dict,
    ):
        self._name = state_dict["Name"]
        self._specialization = state_dict["Specialization"]
        self._grades = state_dict["Grades"]

    def load_json(self, filename: str = "student.json"):
        with open(filename) as f_in:
            state_dict = json.load(f_in)

        self._set_state_dict(state_dict)

    def save_pickle(self, filename: str = "student.pickle"):
        with open(filename, "w") as f_out:
            pickle.dump(self._get_state_dict(), f_out)

    def load_pickle(self, filename: str = "student.pickle"):
        with open(filename) as f_in:
            state_dict = pickle.load(f_in)

        self._set_state_dict(state_dict)


# student1 = Student("John", "IT", [10,9])
# student2 = Student("Anna", "Biology", [5,9])
# student3 = Student("Yana", "Math", [12,7])
#
# student3.save_json("student3.json")
# student3.load_json("student3.json")


# Завдання 1
# Напишіть програму для збереження даних про музичні
# групи у вигляді словника, де ключ – назва групи, значення –
# список альбомів.
# Напишіть функціонал:
#  додати новий гурт
#  додати новий альбом
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle


# ADD FRIENDS
def add_friends(friends: dict[str, list[str]]):
    friend1 = input("Enter name: ")
    friend2 = input("Enter name: ")

    if friend1 not in friends:
        friends[friend1] = []

    if friend2 not in friends:
        friends[friend2] = []

    friends[friend1].append(friend2)
    friends[friend2].append(friend1)


# SAVE JSON
def save_json(
    friends: dict[str, list[str]],
    filename: str = "friends.json",
):
    with open(filename, "w", encoding="utf-8") as f_out:
        json.dump(friends, f_out, indent=4, ensure_ascii=False)


# LOAD JSON
def load_json(filename: str = "friends.json") -> dict[str, list[str]]:
    with open(filename, encoding="utf-8") as f_in:
        return json.load(f_in)


# SAVE PICKLE
def save_pickle(
    friends: dict[str, list[str]],
    filename: str = "friends.pickle",
):
    with open(filename, "wb", encoding="utf-8") as f_out:
        pickle.dump(friends, f_out)


# LOAD PICKLE
def load_pickle(filename: str = "friends.pickle") -> dict[str, list[str]]:
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


# friends = {}
# add_friends(friends)
# add_friends(friends)
#
# save_json(friends)
# save_json(friends)
