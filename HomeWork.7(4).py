# Завдання 1
# Є словник з курсами валют, де ключ – назва валюти,
# значення – курс до гривні. Користувач вводить назву валюти,
# суму та назву нової валюти, в яку треба перевести суму.
# Підказка 1: для того щоб перевести, скажімо, 10 доларів у
# євро, спочатку треба перевести 10 доларів у гривні, після чого
# гривні переводити у євро.
# Підказка 2: щоб можна було переводити долари у
# гривні(або гривні у долари), потрібно щоб у словнику була
# інформація скільки гривень в 1 гривні

# rates = {
#     "UAH": 1,
#     "USD": 40,
#     "EUR": 43
# }
#
# currency_from = input("Enter currency you have: ").upper()
# amount = float(input("Enter amount: "))
# currency_to = input("Enter currency to convert to: ").upper()
#
# if currency_from not in rates or currency_to not in rates:
#     print("Unknown currency!")
#
# else:
#     amount_in_uah = amount * rates[currency_from]
#
#     result = amount_in_uah / rates[currency_to]
#
#     print(f"Result: {result:.2f} {currency_to}")

# Завдання 2
# Напишіть функцію, яка отримує 2 множини з іменами
# працівників, які працюють в офісі та віддалено. Виведіть на
# екран:
#  Імена усіх працівників
#  Імена працівників, які працюють і в офісі, і віддалено
#  Відсоток працівників, які працюють і в офісі, і
# віддалено

# def analyze_workers(office, remote):
#     office_set = set(office)
#     remote_set = set(remote)
#
#     all_workers = office_set | remote_set
#
#     both = office_set & remote_set
#
#     percent = (len(both) / len(all_workers)) * 100 if all_workers else 0
#
#     print("All employees:", all_workers)
#     print("Work both office and remote:", both)
#     print(f"Percentage: {percent:.2f}%")
#
#
# office = {"Anna", "Bob", "Charlie"}
# remote = {"Charlie", "Diana", "Bob"}
#
# analyze_workers(office, remote)
