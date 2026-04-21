# Завдання 1
# Напишіть функцію, яка запитує користувача пароль та
# повертає його. Якщо пароль поганий, тобто менше 8 символів
# чи містить однакові символи то викликати виняток ValueError.
# Написати код try … except який використовує дану
# функцію.
def get_password():
    password = input("Введіть пароль: ")

    if len(password) < 8:
        raise ValueError("Пароль занадто короткий!")

    if len(set(password)) == 1:
        raise ValueError("Пароль не може складатися з однакових символів!")

    return password


try:
    user_password = get_password()
    print("Пароль прийнято:", user_password)

except ValueError as e:
    print("Помилка:", e)


# Завдання 2
# Є словник де ключ – логін, а значення – пароль. Напишіть
# функцію, яка запитує користувача логін та пароль. Якщо
# логіна немає в словнику, або невірний пароль, то викликати
# ValueError.
# Написати код try … except який використовує дану
# функцію.


def login_check(users):
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    if login not in users:
        raise ValueError("Такого логіну не існує!")

    if users[login] != password:
        raise ValueError("Невірний пароль!")

    return True


users_info = {"admin": "12345678", "user1": "password123", "test": "qwerty123"}

try:
    if login_check(users_info):
        print("Вхід успішний!")

except ValueError as e:
    print("Помилка:", e)
