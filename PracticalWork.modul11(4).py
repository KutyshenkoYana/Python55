# Завдання 1
# Створіть клас Message з атрибутами
#  user – ім’я автора повідомлення
#  text – текст повідомлення
#  time – час повідомлення(використайте модуль datetime)
# приклад datetime.strptime('10:23', '%H:%M')
# методи:
#  __str__(self) – повертає текст повідомлення та час
#  __len__(self) – повертає довжину повідомлення
#  __gt__(self, other) – перевіряє чи є повідомлення self
# старішим за other
# Створіть список з декількома повідомленнями та виведіть
# його. Відсортуйте список і знову виведіть

# import datetime
#
# class Message:
#     def __init__(self, user:str, text:str, time:str):
#         self._user = user
#         self._text = text
#         self._time = datetime.datetime.strptime(time, '%H:%M')
#
#
#     def __str__(self):
#         return (f"User: {self._user}, Text: {self._text}, "
#                 f"Time: {self._time.strftime('%H:%M')}")
#
#
#     def __len__(self):
#         return len(self._text)
#
#
#     def __gt__(self, other):
#         return self._time > other._time
#
#
# message = Message("Yana123", "Hello!", "19:10")
# message2 = Message("Maks555", "Hiii", "20:18")
#
# print(message)
# print(len(message))
#
# print(message2 > message)
#
# messages = []
# messages.append(Message("Yana123", "Hello!", "19:10"))
# messages.append(Message("Maks555", "Hiii", "20:18"))
# messages.append(Message("Kamila000", "How are you?", "23:10"))
# messages.append(Message("George", "Gooddd:)))", "23:55"))
#
# for message in messages:
#     print(message)
#
# messages.sort()
#
# for message in messages:
#     print(message)


# Завдання 2
# Створіть клас Song з атрибутами
#  name – назва пісні
#  author – ім’я автора
# Практичне завдання
# методи:
#  __eq__(self, other) – перевіряє чи дві пісні однакові
#  __str__(self, other) – повертає рядок з назвою та автором
# Створіть клас Playlist з атрибутами
#  songs – список пісень(об’єкти класу Song)

# методи:
#  __len__(self) – повертає кількість пісень
#  __contains__(self, item) – перевіряє чи є пісня в плейлисті
#  __iter__(self) – повертає літератор для циклу for
#  add_song(self, song) – додає пісню в плейлист
#  remove_song(self, song) – видаляє пісню з плейлиста
# Створіть порожній плейлист
# Створіть 3 пісні:
# "Imagine", "John Lennon"
# "Bohemian Rhapsody", "Queen"
# "Shape of You", "Ed Sheeran"
# Добавте їх в плейлист
# Пройдіться циклом for по плейлисту та виведіть кожну
# пісню на екран

# class Song:
#     def __init__(self,name: str, autor: str):
#         self._name = name
#         self._autor = autor
#
#
#     def __eq__(self, other):
#         if isinstance(other, Song):
#             return self._name == other._name and self._autor == other._autor
#
#         return False
#
#
#     def __str__(self):
#         return f"{self._name} by --- {self._autor}"
#
#
# class Playlist:
#     def __init__(self, songs: list[Song]):
#         self._songs = songs
#
#
#     def __len__(self):
#         return len(self._songs)
#
#
#     def __contains__(self, song: Song):
#         return song in self._songs
#
#
#     def __iter__(self):
#         return iter(self._songs)
#
#
#     def add_song(self, song: Song):
#         self._songs.append(song)
#
#
#     def remove_song(self, song: Song):
#         if song in self._songs:
#             self._songs.remove(song)
#
#
# song1 = Song("Imagine", "John Lennon")
# song2 = Song("Bohemian Rhapsody", "Queen")
# song3 = Song("Shape of You", "Ed Sheeran")
#
# playlist = Playlist([song1, song2, song3])
#
# for song in playlist:
#     print(song)


# Завдання 3
# Створіть клас Cart з атрибутами
#  items – список товарів
#  total – загальна ціна товарів
# методи:
#  __str__(self) – повертає рядок зі списком товарів
#  __len__(self) – повертає кількість товарів
#  __add__(self, other) – об’єднує 2 кошики та повертає
# новий кошик
# Створіть два кошики. Виведіть кількість товарів в кожному
# з них. Виведіть самі кошики. Об’єднайте їх та виведіть
# кількість товарів в новому кошику та товари в ньому


# class Cart:
#     def __init__(self, items: list[str], total: int):
#         self._items = items
#         self._total = total
#
#
#     def __str__(self):
#         return f"Items: {self._items} , Price: {self._total}"
#
#
#     def __len__(self):
#         return len(self._items)
#
#
#     def __add__(self, other):
#         return Cart(self._items + other._items, self._total + other._total)
