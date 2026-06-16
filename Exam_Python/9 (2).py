# Симулятор роботи сайту
# WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
# Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
# WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.

from datetime import datetime


class WebPage:
    def __init__(self, title, content):
        self._title = title
        self._content = content
        self._publish_date = datetime.now()

    def show_details(self):
        print("\n---- СТОРІНКА ----")
        print(f"Заголовок: {self._title}")
        print(f"Дата: {self._publish_date.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Вміст:\n{self._content}")


class WebSite:
    def __init__(self, name, url):
        self._name = name
        self._url = url
        self._pages = []

    def add_page(self, page):
        self._pages.append(page)

    def remove_page(self, title):
        for page in self._pages:
            if page._title == title:
                self._pages.remove(page)
                return True
        return False

    def edit_page(self, title, new_content):
        for page in self._pages:
            if page._title == title:
                page._content = new_content
                return True
        return False

    def search_pages(self, keyword):
        result = []
        for page in self._pages:
            if (
                keyword.lower() in page._title.lower()
                or keyword.lower() in page._content.lower()
            ):
                result.append(page)
        return result

    def show_info(self):
        print(f"Сайт: {self._name}")
        print(f"URL: {self._url}")
        print(f"Сторінок: {len(self._pages)}")

        for i, page in enumerate(self._pages, 1):
            print(f"{i}. {page._title}")


class UserSystem:
    def __init__(self):
        self._users = {}
        self._current_user = None

    def register(self, login, password):
        if login in self._users:
            return False
        self._users[login] = password
        return True

    def login(self, login, password):
        if self._users.get(login) == password:
            self._current_user = login
            return True
        return False

    def is_logged_in(self):
        return self._current_user is not None


def main():
    users = UserSystem()
    site = None

    while True:
        print("\n------ Меню --------")
        print("1. Реєстрація")
        print("2. Логін")
        print("3. Створити сайт")
        print("4. Додати сторінку")
        print("5. Видалити сторінку")
        print("6. Редагувати сторінку")
        print("7. Пошук сторінок")
        print("8. Інформація про сайт")
        print("9. Перегляд сторінки")
        print("0. Вихід")

        choice = input("Вибір: ")

        if choice == "1":
            login = input("Логін: ")
            password = input("Пароль: ")

            if users.register(login, password):
                print("Реєстрація успішна :) ")
            else:
                print("Користувач вже існує :(")

        elif choice == "2":
            login = input("Логін: ")
            password = input("Пароль: ")

            if users.login(login, password):
                print("Вхід виконано :) ")
            else:
                print("Невірні дані :( ")

        elif choice == "3":
            if not users.is_logged_in():
                print("Спочатку увійдіть в аккаунт")
                continue

            name = input("Назва сайту: ")
            url = input("URL: ")
            site = WebSite(name, url)
            print("Сайт створено :) ")

        elif choice == "4":
            if not site:
                print("Сайт не створено :( ")
                continue

            title = input("Заголовок: ")
            content = input("Вміст: ")
            site.add_page(WebPage(title, content))
            print("Сторінку додано :) ")

        elif choice == "5":
            if site:
                title = input("Назва сторінки: ")
                if site.remove_page(title):
                    print("Видалено :) ")
                else:
                    print("Не знайдено :( ")

        elif choice == "6":
            if site:
                title = input("Сторінка: ")
                content = input("Новий вміст: ")

                if site.edit_page(title, content):
                    print("Оновлено :) ")
                else:
                    print("Не знайдено :) ")

        elif choice == "7":
            if site:
                keyword = input("Ключове слово: ")
                result = site.search_pages(keyword)

                if not result:
                    print("Нічого не знайдено :( ")
                else:
                    print("\nЗнайдено :) :")
                    for p in result:
                        print("-", p._title)

        elif choice == "8":
            if site:
                site.show_info()

        elif choice == "9":
            if site:
                title = input("Сторінка: ")
                for p in site._pages:
                    if p._title == title:
                        p.show_details()
                        break
                else:
                    print("Не знайдено :( ")

        elif choice == "0":
            print("Вихід ")
            break

        else:
            print("Невірний вибір :( ")


if __name__ == "__main__":
    main()


# Додаткові можливості (за бажанням на кристалики):
# Реалізуйте систему логіну/реєстрації для керування
# сайтом. Додайте можливість редагування існуючих сторінок.
# Створіть функціонал для пошуку сторінок за ключовими
# словами у заголовку або вмісті.
