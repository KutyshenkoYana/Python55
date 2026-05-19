# Завдання 1
# Створіть клас Passenger з атрибутами
#  name – ім’я
#  destination – місце, куди прямує


class Passenger:
    def __init__(self, name, destination):
        self.name = name
        self.destination = destination


# авдання 2
# Створіть клас Transport з атрибутами
#  speed – швидкість
# Методи
#  move(destination, distance) – рухається до місця
# призначення, виводить інформацію як довго їхали


class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self, destination, distance):
        time = distance / self.speed
        print(f"Transport is moving to {destination}.")
        print(f"Travel time: {time:.2f} hours.")


# Завдання 3
# Створіть клас Bus з атрибутами
#  passengers – список пасажирів(об’єкти класу Passenger)
#  capacity – максимальна можлива кількість пасажирів
# Методи
#  board_passenger(passenger) – якщо є місце, додає
# пасажира
#  move(destination, distance) – висаджує всіх пасажирів, які
# хочуть вийти в даному місці(виводить їхню загальну
# кількість) та викликає батьківський метод move()


class Bus(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed)
        self.capacity = capacity
        self.passengers = []

    def board_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            print(f"Passenger {passenger.name} boarded the bus.")
        else:
            print("The bus is full.")

    def move(self, destination, distance):
        leaving_passengers = [
            p for p in self.passengers if p.destination == destination
        ]

        self.passengers = [p for p in self.passengers if p.destination != destination]

        print(f"{len(leaving_passengers)} passengers left the bus at {destination}.")

        super().move(destination, distance)


p1 = Passenger("Ivan", "Kyiv")
p2 = Passenger("Maria", "Lviv")
p3 = Passenger("Oleg", "Kyiv")

bus = Bus(speed=60, capacity=2)

bus.board_passenger(p1)
bus.board_passenger(p2)
bus.board_passenger(p3)

bus.move("Kyiv", 120)
