# Завдання 1
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить максимум у списку.
# Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.

import threading

numbers = []

count = int(input("How many numbers do you want to enter? "))

for i in range(count):
    number = int(input("Enter number: "))
    numbers.append(number)


def find_max():
    print(f"Maximum number: {max(numbers)}")


def find_min():
    print(f"Minimum number: {min(numbers)}")


thread_max = threading.Thread(target=find_max)
thread_min = threading.Thread(target=find_min)

thread_max.start()
thread_min.start()

thread_max.join()
thread_min.join()


# Завдання 2
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить суму елементів
# у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.

import threading

numbers = []

count = int(input("How many numbers do you want to enter? "))

for i in range(count):
    number = int(input("Enter number: "))
    numbers.append(number)


def find_sum():
    print(f"Sum: {sum(numbers)}")


def find_average():
    average = sum(numbers) / len(numbers)
    print(f"Average: {average}")


thread_sum = threading.Thread(target=find_sum)
thread_average = threading.Thread(target=find_average)

thread_sum.start()
thread_average.start()

thread_sum.join()
thread_average.join()


# Завдання 3
# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.

import threading

path = input("Enter file path: ")

with open(path) as file:
    numbers = list(map(int, file.read().split()))


def write_even():
    even_numbers = [num for num in numbers if num % 2 == 0]

    with open("even.txt", "w") as file:
        file.write(" ".join(map(str, even_numbers)))

    print(f"Even numbers count: {len(even_numbers)}")


def write_odd():
    odd_numbers = [num for num in numbers if num % 2 != 0]

    with open("odd.txt", "w") as file:
        file.write(" ".join(map(str, odd_numbers)))

    print(f"Odd numbers count: {len(odd_numbers)}")


thread_even = threading.Thread(target=write_even)
thread_odd = threading.Thread(target=write_odd)

thread_even.start()
thread_odd.start()

thread_even.join()
thread_odd.join()
