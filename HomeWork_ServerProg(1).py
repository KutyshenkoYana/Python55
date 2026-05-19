# Курс: AI+Python
# Модуль 14. Паралельне програмування
# Тема: Паралельне
# програмування. Частина 1
# Завдання 1
# Програма складається з трьох потоків. Перший
# просить в користувача вводити числа, поки не введено
# порожній рядок, та зберігає числа в список.
# Інші два потоки чекають поки перший завершить
# роботу, і вже потім запускаються. Один рахує суму чисел в
# списку, інший рахує середнє арифметичне.
# Список чисел, сума та середнє виводяться на екран

import threading

numbers = []


def input_numbers():
    print("Enter numbers (press Enter to finish):")

    while True:
        value = input("Number: ")

        if value == "":
            break

        numbers.append(float(value))


def calculate_sum():
    total = sum(numbers)
    print(f"\nSum: {total}")


def calculate_average():
    if len(numbers) > 0:
        average = sum(numbers) / len(numbers)
        print(f"Average: {average}")
    else:
        print("No numbers entered.")


thread_input = threading.Thread(target=input_numbers)

thread_input.start()

thread_input.join()

thread_sum = threading.Thread(target=calculate_sum)
thread_average = threading.Thread(target=calculate_average)

thread_sum.start()
thread_average.start()

thread_sum.join()
thread_average.join()

print(f"\nNumbers: {numbers}")
