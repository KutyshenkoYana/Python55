# # Завдання 1
# # Створіть абстрактний клас Robot з атрибутами:
# #  name – назва робота або id
# #  battery_level – рівень заряду(за замовчуванням 100%)
# #  status – поточний стан (один з on, off, working)
# # Методи:
# #  info() – виводить інформацію
# #  charge() – відновлює заряд до 100%
# #  turn_on() – змінює стан на on
# #  turn_off() – змінює стан на off
#
# import uuid
# from enum import Enum
# from abc import ABC
#
#
# class RobotStatus(Enum):
#     off = "off"
#     on = "on"
#
#
# class Robot(ABC):
#     def __init__(
#         self,
#         name: str | None = None,
#         battery_level: int = 100,
#         status: RobotStatus = RobotStatus.off,
#     ):
#         if name is None:
#             name = str(uuid.uuid4())
#
#         self._name = name
#         self._battery_level = battery_level
#         self._status = status
#
#     def info(self):
#         print(f"Robot Name: {self._name}")
#         print(f"Battery Level: {self._battery_level}")
#         print(f"Status: {self._status}")
#
#     def charge(self):
#         self._battery_level = 100
#
#     def turn_on(self):
#         self._status = RobotStatus.on
#
#     def turn_off(self):
#         self._status = RobotStatus.off
#
#
# # Завдання 2
# # Створіть дочірній клас CleaningRobot
# # Додаткові атрибути:
# #  dust_capacity – ємність контейнеру для пилу(за
# # замовчуванням 0%)
# #  water_capacity – ємність контейнеру для води(за
# # замовчуванням 100%)
# #  cleaning_mode – тип прибирання(вологе або сухе)
# # Методи:
# #  info() – додатково виводить інформацію про робота
# # Практичне завдання
# #  turn_on() – якщо контейнер для пилу повний або
# # контейнер для води порожній то виводить повідомлення,
# # інакше запускається turn_on() з класу Robot
# #  empty_dustbin() – очищає контейнер для пилу
# #  fill_water() – заповнює контейнер для води
# #  swap_mode() – змінює тип прибирання на протилежний
# #  clean(energy, dust, water=None) – чистить поверхню,
# # якщо прибирання сухе, то просто перенести пил у
# # контейнер(якщо місця не достатньо вивести помилку),
# # якщо прибирання вологе то додатково витратити воду.
# # Також зменшує рівень заряду на energy
#
#
# class CleaningMode(Enum):
#     dry_cleaning = "dry_cleaning"
#     wet_cleaning = "wet_cleaning"
#
#
# class CleaningRobot(Robot):
#     def __init__(
#         self,
#         name: str | None = None,
#         battery_level: int = 100,
#         dust_capacity: int = 0,
#         water_capacity: int = 100,
#         cleaning_mode: CleaningMode = CleaningMode.dry_cleaning,
#     ):
#         super().__init__(name, battery_level)
#         self._dust_capacity = dust_capacity
#         self._water_capacity = water_capacity
#         self._cleaning_mode = cleaning_mode
#
#     def info(self):
#         super().info()
#         print("Dust Capacity:", self._dust_capacity)
#         print("Water Capacity:", self._water_capacity)
#         print("Cleaning Mode:", self._cleaning_mode)
#
#     def turn_on(self):
#         if self._dust_capacity >= 100 or self._water_capacity <= 0:
#             print("Cannot turn on")
#             return
#
#         super().turn_on()
#
#     def empty_dustbin(self):
#         self._dust_capacity = 0
#
#     def fill_water(self):
#         self._water_capacity = 100
#
#     def swap_mode(self):
#         if self._cleaning_mode == CleaningMode.dry_cleaning:
#             self._cleaning_mode = CleaningMode.wet_cleaning
#
#         else:
#             self._cleaning_mode = CleaningMode.dry_cleaning
#
#     def clean(self, energy: int, dust: int, water: int | None = None):
#         if self._battery_level < energy:
#             print("Not enough energy available")
#             return
#
#         if self._dust_capacity + dust > 100:
#             print("Not enough dust capacity available")
#             return
#
#         self._battery_level -= energy
#         self._dust_capacity += dust
#
#         if self._cleaning_mode == CleaningMode.wet_cleaning:
#             if water is None:
#                 print("Not enough water available")
#                 return
#
#             if self._water_capacity < water:
#                 print("Not enough water available")
#                 return
#
#             self._water_capacity -= water
#
#
# # Завдання 3
# # Створіть дочірній клас SecurityRobot
# # Додаткові атрибути:
# #  min_speed – мінімальна швидкість руху, щоб помітити
# # об’єкт
# #  alert_level – рівень небезпеки (low, middle, high)
# #  dangerous_items – список небезпечних предметів(gun,
# # knife, bat)
# # Методи:
# #  info() – додатково виводить інформацію про робота
# #  turn_off() – перед виключенням змінює рівень небезпеки
# # на low
# #  add_dangerous_item(item) – додає небезпечний предмет
# #  remove_dangerous_item(item) – видаляє небезпечний
# # предмет
# #  detect(speed, item) – виявляє загрозу
# # o якщо швидкість занизька, то ігноруємо
# # o якщо швидкість велика, то рівень небезпеки
# # middle
# # o якщо це небезпечний предмет, то рівень
# # небезпеки high
# # Рівень небезпеки не може стати нижчим
#
#
# class AlertLevel(Enum):
#     low = "low"
#     medium = "medium"
#     high = "high"
#
#
# class SecurityRobot(Robot):
#     dangerous_items = ["gun", "knife", "bat"]
#
#     def __init__(
#         self,
#         name: str | None = None,
#         battery_level: int = 100,
#         min_speed: int = 0,
#         alert_level: AlertLevel = AlertLevel.low,
#         dangerous_items=None,
#     ):
#         super().__init__(name, battery_level)
#         self._min_speed = min_speed
#         self._alert_level = alert_level
#         self._dangerous_items = dangerous_items or self.dangerous_items.copy()
#
#     def info(self):
#         super().info()
#         print(f"Minimum Speed: {self._min_speed}")
#         print(f"Alert Level: {self._alert_level}")
#         print(f"Dangerous Items: {self._dangerous_items}")
#
#     def turn_off(self):
#         self._alert_level = AlertLevel.low
#         super().turn_off()
#
#     def add_dangerous_item(self, item: str):
#         if item not in self._dangerous_items:
#             self._dangerous_items.append(item)
#
#     def remove_dangerous_item(self, item: str):
#         if item in self._dangerous_items:
#             self._dangerous_items.remove(item)
#
#     def detect(self, speed: int, item: str | None = None):
#         if speed < self._min_speed:
#             return
#
#         if self._alert_level != AlertLevel.high:
#             self._alert_level = AlertLevel.medium
#
#         if item and item in self._dangerous_items:
#             self._alert_level = AlertLevel.high
