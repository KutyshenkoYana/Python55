# Завдання 1
# Користувач вводить через кому список товарів. Виведіть
# цей список на екран, але без повторень назв товарів

# user_input = input("Enter products separated by comma: ")
#
# products = user_input.split(",")
# unique_products = set()
#
# for product in products:
#     unique_products.add(product.strip())
#
# print(list(unique_products))

# Завдання 2
# У магазині є два списки клієнтів: ті хто отримав знижкові
# купони, і ті хто ними скористався.
# Напишіть функцію, яка отримує 2 списки та виводить
# інформацію:
#  Імена тих, хто отримав купон, але не скористався,
# також вивести їх кількість
#  Імена шахраїв, які скористались знижкою, але магазин
# не давав їм купони

# def analyze_clients(received, used):
#     received_set = set(received)
#     used_set = set(used)
#
#     not_used = received_set - used_set
#
#     fraud = used_set - received_set
#
#     print("Did not use coupon:", list(not_used))
#     print("Count:", len(not_used))
#
#     print("Fraud clients:", list(fraud))
#
# received = ["Anna", "Bob", "Charlie", "Diana"]
# used = ["Bob", "Charlie", "Eve"]
#
# analyze_clients(received, used)
