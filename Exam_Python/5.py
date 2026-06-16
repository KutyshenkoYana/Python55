# Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.


def capital_strings(strings):
    result = []

    for s in strings:
        if s and s[0].isupper():
            result.append(s)

    return result


words = input("Введіть рядки через пробіл: ").split()

print(capital_strings(words))
