# Завдання 1
# Напишіть гру вгадати число: комп’ютер загадує число
# від 1 до 100. Користувач вводить свої відповіді на що
# отримує підказки більше\менше.
# Якщо число вгадане менш ніж за 5 спроб, то переміг
# користувач, інакше комп’ютер.
# Реалізуйте такий функціонал:
#  почати нову гру – користувач вводить числа до
# правильної відповіді
#  вивести результат – кількість перемог та програшів
#  зберегти дані – зберегти кількості перемог та
# програшів у файл
#  завантажити дані – завантажити кількості перемог
# та програшів
# Реалізуйте все функціями

import json
import random

wins = 0
losses = 0


def new_game():
    global wins, losses

    secret_number = random.randint(1, 100)
    attempts = 0

    print("Guess the number from 1 to 100.")

    while True:
        guess = int(input("Enter your number: "))
        attempts += 1

        if guess < secret_number:
            print("Greater")
        elif guess > secret_number:
            print("Smaller")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")

            if attempts < 5:
                wins += 1
                print("You win!")
            else:
                losses += 1
                print("Computer wins!")

            break


def show_results():
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")


def save_data():
    data = {"wins": wins, "losses": losses}

    with open("results.json", "w") as file:
        json.dump(data, file)

    print("Data saved!")


def load_data():
    global wins, losses

    try:
        with open("results.json") as file:
            data = json.load(file)

            wins = data["wins"]
            losses = data["losses"]

        print("Data loaded!")

    except FileNotFoundError:
        print("File not found!")


while True:
    print("\nMENU")
    print("1 - New Game")
    print("2 - Show Results")
    print("3 - Save Data")
    print("4 - Load Data")
    print("5 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        new_game()
    elif choice == "2":
        show_results()
    elif choice == "3":
        save_data()
    elif choice == "4":
        load_data()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")
