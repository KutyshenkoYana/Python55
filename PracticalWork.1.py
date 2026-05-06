# Завдання 1
# Створіть клас Проект з атрибутами:
#  назва
#  виділений кошторис
#  загальні витрати
#  чи завершений(за замовчуванням False)
#  час виконання(за замовчуванням 0 місяців)
#  список необхідних задач
# Додайте методи:
#  вивід інформації: назва, час виконання, необхідні
# задачі
#  добавити нову задачу
#  розбити задачу на під-задачі: передається назва задачі
# та список під-задач
#  виконати задачу, передається назва, час та ціна
# виконання
#  поповнення кошторису


class Project:
    def __init__(self, name, budget):
        self._name = name
        self._budget = budget
        self._total_cost = 0
        self._is_finished = False
        self._duration_months = 0
        self._tasks = {}

    def show_info(self):
        print(f"Project: {self._name}")
        print(f"Duration: {self._duration_months} months")
        print("Tasks:")
        for task, sub_tasks in self._tasks.items():
            print(f" - {task}: {sub_tasks}")

    def add_task(self, task_name):
        if task_name not in self._tasks:
            self._tasks[task_name] = []
            print(f"Task '{task_name}' added")
        else:
            print("Task already exists")

    def add_subtasks(self, task_name, sub_tasks):
        if task_name in self._tasks:
            self._tasks[task_name].extend(sub_tasks)
            print(f"Subtasks added to '{task_name}'")
        else:
            print("Task not found")

    def complete_task(self, task_name, time, cost):
        if task_name in self._tasks:
            self._duration_months += time
            self._total_cost += cost

            print(f"Task '{task_name}' completed")
            print(f"Time added: {time} months, cost: {cost}")

            del self._tasks[task_name]

            if len(self._tasks) == 0:
                self._is_finished = True
                print("Project is completed")
        else:
            print("Task not found")

    def add_budget(self, amount):
        self._budget += amount
        print(f"Budget increased by {amount}")


project = Project("Website", 10000)

project.add_task("Design")
project.add_task("Backend")

project.add_subtasks("Design", ["UI", "Logo"])

project.complete_task("Design", 2, 1500)

project.add_budget(5000)

project.show_info()


# Завдання 2
# Створіть клас Телефон з атрибутами:
#  максимальний обсяг пам’яті
# Практичне завдання
#  зайнята пам’ять
#  чи включений(за замовчуванням False)
#  встановлені додатки у вигляді словника, де ключ –
# назва додатку, значення – обсяг пам’яті
# Додайте методи:
#  вивести інформацію про використання пам’яті
#  видалити додаток
#  встановити новий додаток, якщо пам’яті достатньо
#  оновити додаток(нова версія може займати іншу
# кількість пам’яті)
#  запустити додаток, якщо він є і якщо телефон
# вкючений
#  включити телефон
#  виключити телефон


class Phone:
    def __init__(self, max_memory):
        self._max_memory = max_memory
        self._used_memory = 0
        self._is_on = False
        self._apps = {}

    def show_memory_info(self):
        print(f"Max memory: {self._max_memory} MB")
        print(f"Used memory: {self._used_memory} MB")
        print(f"Free memory: {self._max_memory - self._used_memory} MB")
        print("Installed apps:", self._apps)

    def install_app(self, app_name, size):
        if self._used_memory + size <= self._max_memory:
            self._apps[app_name] = size
            self._used_memory += size
            print(f"App '{app_name}' installed")
        else:
            print("Not enough memory")

    def delete_app(self, app_name):
        if app_name in self._apps:
            self._used_memory -= self._apps[app_name]
            del self._apps[app_name]
            print(f"App '{app_name}' deleted")
        else:
            print("App not found")

    def update_app(self, app_name, new_size):
        if app_name in self._apps:
            old_size = self._apps[app_name]
            diff = new_size - old_size

            if self._used_memory + diff <= self._max_memory:
                self._apps[app_name] = new_size
                self._used_memory += diff
                print(f"App '{app_name}' updated")
            else:
                print("Not enough memory for update")
        else:
            print("App not found")

    def run_app(self, app_name):
        if not self._is_on:
            print("Phone is OFF")
            return

        if app_name in self._apps:
            print(f"Running '{app_name}'...")
        else:
            print("App not installed")

    def turn_on(self):
        self._is_on = True
        print("Phone is ON")

    def turn_off(self):
        self._is_on = False
        print("Phone is OFF")
