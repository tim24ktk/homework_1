"""
    Напишите программу, которая принимает на вход координаты двух точек
     и находит расстояние между ними в 2D пространстве.

    Пример:
    - A (3,6); B (2,1) -> 5,09
    - A (7,-5); B (1,-1) -> 7,21
"""


# функция принимает данные от пользователя

def get_coordinat(point):
    return input(f'Введите координаты точки {point} через запятую: ')


def get_distance(a, b):
    first = a.split(',')
    second = b.split(',')
    result = abs(round(((int(second[0]) - int(first[0]))**2 + (int(second[1]) - int(first[1]))**2) ** 0.5, 2))

    return result


a = get_coordinat('A')
b = get_coordinat('B')
distance = get_distance(a, b)
print(f'Расстояние между точками A и B 2D пространстве: {distance}')
