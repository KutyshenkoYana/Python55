# Завдання 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами
# client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик


class Cart:
    def __init__(self, client):
        self._client = client
        self._items = []

    def add_item(self, item):
        self._items.append(item)
        print(f"Item '{item}' added to cart")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            print(f"Item '{item}' removed from cart")
        else:
            print(f"Item '{item}' not found in cart")

    def show_cart(self):
        print(f"Client: {self._client}")
        print("Items:", self._items)


cart = Cart("John")

cart.add_item("Bread")
cart.add_item("Milk")
cart.add_item("Apple")

cart.remove_item("Milk")

cart.show_cart()


# Завдання 2
# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона(на скільки
# зменшити відсотків передається як параметр), якщо він
# опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон.


class Phone:
    def __init__(self, number, battery_level):
        self._number = number
        self._battery_level = battery_level

    def use_battery(self, percent):
        self._battery_level -= percent

        if self._battery_level < 0:
            self._battery_level = 0

        if self._battery_level < 20:
            print("Battery is below 20%! Please charge your phone")

    def show_info(self):
        print(f"Number: {self._number}")
        print(f"Battery level: {self._battery_level}%")


phone = Phone("+380123456789", 50)

phone.use_battery(20)
phone.use_battery(15)

phone.show_info()
