# Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".


def find_python(strings):
    result = []

    for s in strings:
        if "Python" in s:
            result.append(s)

    return result


words = input("Введіть рядки через пробіл: ").split()

print(find_python(words))
