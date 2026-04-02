# Завдання 1
# Реалізуйте роботу банку. Усі дані зберігаються у
# словнику, де ключ – ім’я клієнта, значення – баланс на
# рахунку.
# Напишіть функцію, яка отримує словник з даними та
# зараховує гроші на баланс. Для цього вона запитує ім’я та
# суму у користувача, якщо користувача немає, то вносить його
# дані у словник, інакше додає суму до балансу.
# Напишіть іншу функцію, яка отримує словник з даними та
# знімає гроші з рахунку. Для цього вона запитує ім’я та суму у
# користувача, якщо користувача немає, то вивести відповідне
# повідомлення. Якщо на балансі не достатньо грошей, теж
# вивести повідомлення.
# Напишіть функцію main, яка організує роботу всієї
# програми, а саме матиме такий функціонал: поповнити
# рахунок, зняти кошти, завершити роботу

# def deposit(accounts):
#     name = input("Enter name: ")
#     amount = float(input("Enter amount to deposit: "))
#
#     if name in accounts:
#         accounts[name] += amount
#     else:
#         accounts[name] = amount
#
#     print(f"Balance for {name}: {accounts[name]}")
#
#
# def withdraw(accounts):
#     name = input("Enter name: ")
#     amount = float(input("Enter amount to withdraw: "))
#
#     if name not in accounts:
#         print("Client not found!")
#         return
#
#     if accounts[name] < amount:
#         print("Not enough money!")
#         return
#
#     accounts[name] -= amount
#     print(f"Balance for {name}: {accounts[name]}")
#
#
# def main():
#     accounts = {}
#
#     while True:
#         print("\n1. Deposit")
#         print("2. Withdraw")
#         print("3. Exit")
#
#         choice = input("Choose option: ")
#
#         if choice == "1":
#             deposit(accounts)
#         elif choice == "2":
#             withdraw(accounts)
#         elif choice == "3":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid option!")
#
#
# main()
