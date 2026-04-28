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


products = []

add_products(products)
add_products(products)

save_products_json(products)
save_products_pickle(products)

load_products_json(filename="products.json")
load_products_pickle(filename="products.pickle")
