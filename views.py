from unittest import result


def user_menu():
    menu = ['Показать всех животных', 'Добавить животное',
            'Удалить животное']
    for item in enumerate(menu, 1):
        print(*item)
    num = int(input('Выберите пункт меню: '))
    return num


def show_all_animals(data):
    for item in data:
        print(item)


def add_animals():
    name = input('Введите кличку: ')
    comands = input('Введите команды: ')
    birthday = input('Введите дату рождения: ')
    typ = input('Введите вид: ')
    arr = [name, comands, birthday, typ]
    return arr


def del_animal():
    num = int(input('Введите id животного, которого хотите удалить: '))
    return num
