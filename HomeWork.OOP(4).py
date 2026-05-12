# Завдання 1
# Створіть клас Recipe з атрибутами
#  name – назва страви
#  ingredients – список продуктів
#  text – текст рецепту
#  time – час приготування
# методи:
#  __str__(self) – повертає назву страви
#  __contains__(self, item) – перевіряє чи є інгредієнт в
# рецепті
#  __gt__(self, other) – перевіряє чи є час приготування self
# більшим за other
#  display_info(self) – виводить всю інформацію про рецепт
# Створіть декілька рецептів та добавте їх у список.
# Виведіть назви тих рецептів, які містять інгредієнт томат
# Виведіть повну інформацію рецепта з найменшим часом
# приготування, скористайтесь функцією min
# Приклад рецептів:
# Recipe("Піца",
# Домашнє завдання
#  ["борошно", "вода", "дріжджі", "томат", "сир"],
#  "Готуємо тісто, додаємо інгредієнти та запікаємо",
#  30)
#
#  Recipe("Салат",
#  ["томат", "огірок", "зелень", "олія"],
#  "Нарізаємо овочі, додаємо зелень та поливаємо
# олією",
#  10)
#
#  Recipe("Суп",
#  ["вода", "картопля", "морква", "м'ясо"],
#  "Варимо всі інгредієнти до готовності",
#  45)


class Recipe:
    def __init__(self, name, ingredients, text, time):
        self._name = name
        self._ingredients = ingredients
        self._text = text
        self._time = time

    def __str__(self):
        return self._name

    def __contains__(self, item):
        return item in self._ingredients

    def __gt__(self, other):
        return self._time > other._time

    def display_info(self):
        print(f"Name: {self._name}")
        print(f"Ingredients: {self._ingredients}")
        print(f"Recipe: {self._text}")
        print(f"Cooking time: {self._time} minutes")


recipe1 = Recipe(
    "Pizza",
    ["flour", "water", "yeast", "tomato", "cheese"],
    "Prepare dough, add ingredients and bake",
    30,
)

recipe2 = Recipe(
    "Salad",
    ["tomato", "cucumber", "greens", "oil"],
    "Cut vegetables, add greens and oil",
    10,
)

recipe3 = Recipe(
    "Soup",
    ["water", "potato", "carrot", "meat"],
    "Boil all ingredients until ready",
    45,
)


recipes = [recipe1, recipe2, recipe3]


print("Recipes with tomato:")

for recipe in recipes:
    if "tomato" in recipe:
        print(recipe)


fastest_recipe = min(recipes, key=lambda recipe: recipe._time)

print("\nFastest recipe:")
fastest_recipe.display_info()
