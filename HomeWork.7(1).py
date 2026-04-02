# Завдання 1
# Є кортеж з назвами міст. Виведіть ті міста, які
# зустрічаються в кортежі більше одного разу.

# cities = ("Kyiv", "Lviv", "Odesa", "Kyiv", "Kharkiv", "Lviv", "Dnipro")
#
# repeated = set()
#
# for city in cities:
#     if cities.count(city) > 1:
#         repeated.add(city)
#
# print(repeated)

# Завдання 2
# Є два кортежі з випадковими числами. Виведіть на екран
# ті числа, які є в першому кортежі, але немає в другому.

# tuple1 = (1, 2, 3, 4, 5, 6)
# tuple2 = (4, 5, 6, 7, 8, 9)
#
# result = []
#
# for num in tuple1:
#     if num not in tuple2:
#         result.append(num)
#
# print(result)

# Завдання 3
# Напишіть функцію, яка отримує 2 кортежі. Поверніть
# список з елементами, які є в обох кортежах і мають однакові
# індекси. Підказка: використайте zip()


# def same_index_elements(t1, t2):
#     result = []
#
#     for a, b in zip(t1, t2, strict=False):
#         if a == b:
#             result.append(a)
#
#     return result
#
#
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (1, 0, 3, 9, 5)
#
# print(same_index_elements(tuple1, tuple2))
