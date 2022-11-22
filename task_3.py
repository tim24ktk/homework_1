"""
    Напишите программу, которая принимает на вход координаты точки (X и Y),
    причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
    в которой находится эта точка (или на какой оси она находится).

    Пример:
    - x=34; y=-30 -> 4
    - x=2; y=4-> 1
    - x=-34; y=-30 -> 3
"""


# функция принимает данные от пользователя

def get_coordinat(axis):
    return int(input(f'Введите точку {axis}: '))


# функция получает номер четверти в плоскости

def get_quarter_number(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        return 0


x = get_coordinat('X')
y = get_coordinat('Y')
quarter_number = get_quarter_number(x, y)

if quarter_number == 0:
    print('Такой четверти не существует или точка находится на одной из осей!')
else:
    print(f'Точка находится в {quarter_number}-й четверти')
