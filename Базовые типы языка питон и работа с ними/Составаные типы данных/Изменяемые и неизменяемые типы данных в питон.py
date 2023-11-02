# TODO исправьте опечатку в слове
fruits = ["яблоко", "банан", "опельсин", "виноград"]
a_fruit = fruits[2]
new_fruit = "а" + a_fruit[1:]
fruits[2] = new_fruit
print(fruits)