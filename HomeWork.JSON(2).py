# Курс: AI+Python
# Модуль 13. Пакування даних
# Тема: Pickle. Частина 2
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


import json
import pickle

bands = {}


def add_band():
    name = input("Enter band name: ")

    if name not in bands:
        bands[name] = []
        print("Band added.")
    else:
        print("Band already exists.")


def add_album():
    name = input("Enter band name: ")

    if name in bands:
        album = input("Enter album name: ")
        bands[name].append(album)
        print("Album added.")
    else:
        print("Band not found.")


def show_data():
    if not bands:
        print("No data available.")
    else:
        for band, albums in bands.items():
            print(f"\n{band}:")
            for album in albums:
                print(f"- {album}")


def save_json():
    with open("bands.json", "w") as file:
        json.dump(bands, file)

    print("Data saved to JSON.")


def load_json():
    global bands

    try:
        with open("bands.json") as file:
            bands = json.load(file)

        print("Data loaded from JSON.")

    except FileNotFoundError:
        print("JSON file not found.")


def save_pickle():
    with open("bands.pkl", "wb") as file:
        pickle.dump(bands, file)

    print("Data saved to Pickle.")


def load_pickle():
    global bands

    try:
        with open("bands.pkl", "rb") as file:
            bands = pickle.load(file)

        print("Data loaded from Pickle.")

    except FileNotFoundError:
        print("Pickle file not found.")


while True:
    print("\nMENU")
    print("1 - Add new band")
    print("2 - Add new album")
    print("3 - Show data")
    print("4 - Save to JSON")
    print("5 - Save to Pickle")
    print("6 - Load from JSON")
    print("7 - Load from Pickle")
    print("8 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_band()
    elif choice == "2":
        add_album()
    elif choice == "3":
        show_data()
    elif choice == "4":
        save_json()
    elif choice == "5":
        save_pickle()
    elif choice == "6":
        load_json()
    elif choice == "7":
        load_pickle()
    elif choice == "8":
        print("Goodbye.")
        break
    else:
        print("Invalid option.")
