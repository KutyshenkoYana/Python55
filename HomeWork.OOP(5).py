# Завдання 1
# Створіть клас Pet з атрибутами
#  name – ім’я тварини
#  satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
#  energy – рівень енергії (від 0 до 100, за замовчуванням 50)
# Методи:
#  sleep() – збільшує energy до 100
#  eat(food_amont) – їсть, збільшує satiety на food_amount
#  play(activity_level) – абстрактний метод
#  make_sound() – просто pass

# Створіть клас Cat
# Методи:
#  play(activity_level) – якщо satiety > 60, зменшує energy на
# 2*acticity_level та satiety на acticity_level
#  make_sound() – виводить ‘Мяу’
#  catch_mouse() – якщо energy > 30, ловить мишу. Якщо
# satiety > 40, то грається з мишею, інакше їсть

# Створіть клас Dog
# Методи:
#  play(activity_level) – якщо satiety > 15, зменшує energy на

# Домашнє завдання
# acticity_level//2 та satiety на acticity_level//2
#  make_sound() – виводить ‘Гав’
#  fetch_ball() – ловить м’яча якщо satiety>10, зменшує
# energy на 5


from abc import ABC, abstractmethod


class Pet(ABC):
    def __init__(self, name, satiety=50, energy=50):
        self._name = name
        self._satiety = satiety
        self._energy = energy

    def sleep(self):
        self._energy = 100
        print(f"{self._name} is sleeping")

    def eat(self, food_amount):
        self._satiety += food_amount

        if self._satiety > 100:
            self._satiety = 100

        print(f"{self._name} ate food")

    @abstractmethod
    def play(self, activity_level):
        pass

    def make_sound(self):
        pass


class Cat(Pet):
    def play(self, activity_level):
        if self._satiety > 60:
            self._energy -= 2 * activity_level
            self._satiety -= activity_level

            if self._energy < 0:
                self._energy = 0

            if self._satiety < 0:
                self._satiety = 0

            print(f"{self._name} is playing")
        else:
            print(f"{self._name} is too hungry")

    def make_sound(self):
        print("Meooow")

    def catch_mouse(self):
        if self._energy > 30:
            if self._satiety > 40:
                print(f"{self._name} is playing with mouse")
            else:
                print(f"{self._name} ate the mouse")
        else:
            print(f"{self._name} is too tired")


class Dog(Pet):
    def play(self, activity_level):
        if self._satiety > 15:
            self._energy -= activity_level // 2
            self._satiety -= activity_level // 2

            if self._energy < 0:
                self._energy = 0

            if self._satiety < 0:
                self._satiety = 0

            print(f"{self._name} is playing")
        else:
            print(f"{self._name} is too hungry")

    def make_sound(self):
        print("Gaaaff")

    def fetch_ball(self):
        if self._satiety > 10:
            self._energy -= 5

            if self._energy < 0:
                self._energy = 0

            print(f"{self._name} fetched the ball")
        else:
            print(f"{self._name} is too hungry")


# Використання

cat = Cat("Murka")

cat.make_sound()
cat.eat(20)
cat.play(10)
cat.catch_mouse()
cat.sleep()


dog = Dog("Sharik")

dog.make_sound()
dog.eat(15)
dog.play(8)
dog.fetch_ball()
dog.sleep()
