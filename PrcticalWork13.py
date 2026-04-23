# # Завдання 1
# # Є словник з логінами(ключ) та паролями(значення)
# # користувачів. Реалізуйте програму яка дозволяє:
# #  завантажити дані з файлу
# #  зберегти дані у файл
# #  додати нового користувача
# #  видалити користувача
# #  зміна паролю
# #  вхід у систему(якщо логін і пароль правильні)
# # Реалізуйте все через функції.
#
# import json
#
#
# def load_data(filename: str = "password.json") -> dict[str, str]:
#     try:
#         with open(filename, encoding="utf-8") as file:
#             data = json.load(file)
#             return data
#
#     except FileNotFoundError:
#         return {}
#
#
# def save_data(data: dict[str, str], filename: str = "password.json") -> None:
#     with open(filename, "w", encoding="utf-8") as file:
#         json.dump(data, file, ensure_ascii=False, indent=4)
#
#
# def add_user(data) -> None:
#     login = input("Enter your login: ")
#
#     if login in data:
#         print("User exists")
#         return
#
#     password = input("Enter your password: ")
#     data[login] = password
#     print("User added")
#
#
# def delete_user(data) -> None:
#     login = input("Enter your login: ")
#
#     if login not in data:
#         print("User does not exist")
#         return
#
#     del data[login]
#     print("User deleted")
#
#
# def change_password(data: dict[str, str]):
#     login = input("Enter your login: ")
#
#     if login not in data:
#         print("User does not exist")
#         return
#
#     new_password = input("Enter new password: ")
#     data[login] = new_password
#     print("Password changed")
#
#
# def login_user(data: dict[str, str]):
#     login = input("Enter your login: ")
#     password = input("Enter your password: ")
#
#     if login in data and data[login] == password:
#         print("Login successful")
#
#     else:
#         print("Incorrect login or password")
#
#
# def main() -> None:
#     data = load_data()
#
#     while True:
#         print("\n1 - Add user")
#         print("2 - Delete user")
#         print("3 - Change password")
#         print("4 - Login")
#         print("5 - Save data")
#         print("0 - Exit")
#
#         choice = input("Choose option: ")
#
#         if choice == "1":
#             add_user(data)
#
#         elif choice == "2":
#             delete_user(data)
#
#         elif choice == "3":
#             change_password(data)
#
#         elif choice == "4":
#             login_user(data)
#
#         elif choice == "5":
#             save_data(data)
#             print("Data saved")
#
#         elif choice == "0":
#             save_data(data)
#             print("Goodbye")
#             break
#
#         else:
#             print("Invalid choice")
#
#
# if __name__ == "__main__":
#     main()
#
#
# # Завдання 2
# # Створіть клас Cart
# # Атрибути:
# #  user – ім’я користувача
# #  items – список товарів
# #  total – загальна ціна
# # Методи:
# #  add(item, price) – добавити товар у кошик
# #  delete(item, price) – видалити товар з кошика
# #  info() – вивести інформацію про кошик
# # Практичне завдання
# #  save(fiename) – зберегти дані у файл(за
# # замовчуванням cart.json)
# #  load(fiename) – завантажити дані з файла(за
# # замовчуванням cart.json)
#
#
# class Cart:
#     def __init__(
#         self,
#         user: str,
#     ):
#         self._user = user
#         self._total = 0
#         self._items = []
#
#     def add(
#         self,
#         item: str,
#         price: int,
#     ):
#         self._items.append(item)
#         self._total += price

# def delete(
#         self, item: str, price: int):
