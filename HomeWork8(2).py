# Завдання 1
# Є текстовий файл. Запишіть в інший файл таку
# статистику:
#  Кількість символів
#  Кількість рядків
#  Кількість цифр
#  Кількість голосних літер(aeuio)

with open("input.txt", encoding="utf-8") as f:
    text = f.read()

chars = len(text)
lines = text.count("\n") + 1 if text else 0
digits = sum(c.isdigit() for c in text)
vowels = sum(c.lower() in "aeuio" for c in text)

print("Символи:", chars)
print("Рядки:", lines)
print("Цифри:", digits)
print("Голосні:", vowels)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(f"Символи: {chars}\n")
    f.write(f"Рядки: {lines}\n")
    f.write(f"Цифри: {digits}\n")
    f.write(f"Голосні: {vowels}\n")


# Завдання 2
# Користувач вводить слово та назву файлу. Виведіть
# кількість цього слова у файлі.

word = input("Введи слово: ")
filename = input("Введи назву файлу: ")

with open(filename, encoding="utf-8") as f:
    text = f.read()

count = text.lower().split().count(word.lower())

print("Кількість входжень:", count)


# Завдання 3
# Є текстовий файл. Видаліть з нього останній рядок.

# filename = input("Введи назву файлу: ")
#
# with open(filename, encoding="utf-8") as f:
#     lines = f.readlines()
#
# lines = lines[:-1]
#
# with open(filename, "w", encoding="utf-8") as f:
#     f.writelines(lines)
#
# print("Останній рядок видалено")
