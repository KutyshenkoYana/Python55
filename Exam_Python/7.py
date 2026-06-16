# (додаткове на кристалики)Напишіть програму, яка
# створює словник, де ключами є слова, а значеннями - їхні
# визначення. Дозвольте користувачу додавати, видаляти
# та шукати слова у цьому словнику.

dictionary = {}

while True:
    print("\n1 - Додати слово")
    print("2 - Знайти слово")
    print("3 - Видалити слово")
    print("4 - Показати всі слова")
    print("0 - Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        word = input("Слово: ")
        definition = input("Значення: ")
        dictionary[word] = definition
        print("Додано до словнику :) ")

    elif choice == "2":
        word = input("Яке слово шукаєте? ")
        if word in dictionary:
            print("Значення:", dictionary[word])
        else:
            print("Слова немає :( ")

    elif choice == "3":
        word = input("Яке слово хочете видалити? ")
        if word in dictionary:
            del dictionary[word]
            print("Cлово видалено")
        else:
            print("Слова немає :( ")

    elif choice == "4":
        for word in dictionary:
            print(word, ":", dictionary[word])

    elif choice == "0":
        break

    else:
        print("Невірний вибір :( ")
