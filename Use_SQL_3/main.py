# Завдання 1
# Створіть додаток «Соціальна мережа», який зберігає
# інформацію про користувача, його друзів, публікації користувача. Можливості додатку:
# ■ вхід за логіном і паролем;
# ■ додати користувача;
# ■ видалити користувача;
# ■ редагувати інформацію про користувача;
# ■ пошук користувача за ПІБ;
# ■ перегляд інформації про користувача;
# ■ перегляд усіх друзів користувача;
# ■ перегляд усіх публікацій користувача.
# Зберігайте дані у базі даних NoSQL. Можете використовувати Redis в якості платформи.

import redis

r = redis.Redis(host="localhost", port=6379, decode_responses=True)


def create_user():
    username = input("Login: ")

    if r.exists(f"user:{username}"):
        print("User already exists.")
        return

    password = input("Password: ")
    full_name = input("Full name: ")
    age = input("Age: ")
    country = input("Country: ")

    r.hset(
        f"user:{username}",
        mapping={
            "password": password,
            "full_name": full_name,
            "age": age,
            "country": country,
        },
    )

    print("User created.")


def delete_user():
    username = input("Login of user to delete: ")

    if not r.exists(f"user:{username}"):
        print("User not found.")
        return

    r.delete(f"user:{username}")
    r.delete(f"friends:{username}")
    r.delete(f"posts:{username}")

    print("User deleted.")


def edit_user():
    username = input("Login of user: ")

    if not r.exists(f"user:{username}"):
        print("User not found.")
        return

    full_name = input("New full name: ")
    age = input("New age: ")
    country = input("New country: ")

    r.hset(
        f"user:{username}",
        mapping={"full_name": full_name, "age": age, "country": country},
    )

    print("User information updated.")


def search_user():
    full_name = input("Full name: ")
    users = r.keys("user:*")

    found = False

    for key in users:
        if r.hget(key, "full_name") == full_name:
            username = key.split(":", 1)[1]
            print(f"Login: {username}")
            print(f"Full name: {r.hget(key, 'full_name')}")
            print(f"Age: {r.hget(key, 'age')}")
            print(f"Country: {r.hget(key, 'country')}")
            print()
            found = True

    if not found:
        print("User not found.")


def show_user():
    username = input("Login of user: ")

    if not r.exists(f"user:{username}"):
        print("User not found.")
        return

    data = r.hgetall(f"user:{username}")

    print(f"Login: {username}")
    print(f"Full name: {data.get('full_name')}")
    print(f"Age: {data.get('age')}")
    print(f"Country: {data.get('country')}")


def add_friend():
    username = input("Your login: ")
    friend = input("Friend login: ")

    if not r.exists(f"user:{username}") or not r.exists(f"user:{friend}"):
        print("User not found.")
        return

    r.sadd(f"friends:{username}", friend)
    r.sadd(f"friends:{friend}", username)

    print("Friend added.")


def show_friends():
    username = input("Login: ")

    if not r.exists(f"user:{username}"):
        print("User not found.")
        return

    friends = r.smembers(f"friends:{username}")

    if not friends:
        print("No friends.")
        return

    print("Friends:")

    for friend in friends:
        print(friend)


def add_post():
    username = input("Login: ")

    if not r.exists(f"user:{username}"):
        print("User not found.")
        return

    text = input("Post: ")
    r.rpush(f"posts:{username}", text)

    print("Post added.")


def show_posts():
    username = input("Login: ")

    if not r.exists(f"user:{username}"):
        print("User not found.")
        return

    posts = r.lrange(f"posts:{username}", 0, -1)

    if not posts:
        print("No posts.")
        return

    print("Posts:")

    for post in posts:
        print(post)


def login():
    username = input("Login: ")
    password = input("Password: ")

    if not r.exists(f"user:{username}"):
        print("User not found.")
        return False

    if r.hget(f"user:{username}", "password") != password:
        print("Wrong password.")
        return False

    print("Login successful.")
    return True


def menu():
    while True:
        print()
        print("1. Add user")
        print("2. Delete user")
        print("3. Edit user")
        print("4. Search user by full name")
        print("5. Show user information")
        print("6. Add friend")
        print("7. Show friends")
        print("8. Add post")
        print("9. Show posts")
        print("0. Logout")

        choice = input("Choose: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            delete_user()
        elif choice == "3":
            edit_user()
        elif choice == "4":
            search_user()
        elif choice == "5":
            show_user()
        elif choice == "6":
            add_friend()
        elif choice == "7":
            show_friends()
        elif choice == "8":
            add_post()
        elif choice == "9":
            show_posts()
        elif choice == "0":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")


def main():
    if not r.exists("user:admin"):
        r.hset(
            "user:admin",
            mapping={
                "password": "1234",
                "full_name": "Admin User",
                "age": "20",
                "country": "Czechia",
            },
        )

    while True:
        print()
        print("SOCIAL NETWORK")
        print("1. Login")
        print("2. Register")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            if login():
                menu()
        elif choice == "2":
            create_user()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
