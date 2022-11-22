"""
    Напишите программу, которая по заданному номеру четверти,
    показывает диапазон возможных координат точек в этой четверти (x и y).
"""


# функция принимает данные от пользователя

def get_quarter_number():
    return int(input(f'Введите номер четверти: '))


# функция по номеру четверти показывает диапозон возможных координат

def get_coordinates(quarter):
    if 0 < quarter <= 4:
        if quarter == 1:
            return f'Диапазон возможных координат точек в {quarter}-й четверти: x от 0 до +∞ и y от 0 до +∞'
        elif quarter == 2:
            return f'Диапазон возможных координат точек в {quarter}-й четверти: x от 0 до -∞ и y от 0 до +∞'
        elif quarter == 3:
            return f'Диапазон возможных координат точек в {quarter}-й четверти: x от 0 до -∞ и y от 0 до -∞'
        elif quarter == 4:
            return f'Диапазон возможных координат точек в {quarter}-й четверти: x от 0 до +∞ и y от 0 до -∞'
    else:
        return 'Введите правильный номер четверти от 1 до 4'


quarter_number = get_quarter_number()

print(get_coordinates(quarter_number))
