users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

list = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}
list["Общее количество"] = len(users)
list["Уникальные посещения"] = len(set(users))
print(list)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
