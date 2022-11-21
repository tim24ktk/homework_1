"""
  Напишите программу, которая принимает на вход цифру,
  обозначающую день недели, и проверяет, является ли этот день выходным.

  Пример:
  - 6 -> да
  - 7 -> да
  - 1 -> нет
"""


# функция получения данных от пользователя
def read_data(line):
    print(line)
    day_number = input()
    return day_number


# функция проверяет является ли день выходным
def check_day_off(day_number):
    if 0 < day_number <= 7:
        if day_number == 6 or day_number == 7:
            return 'Выходной день'
        else:
            return 'Не выходной'
    else:
        return 'Такого дня недели не существует!'


# проверяем работу написанных функций
input_number = int(read_data('Введите число от 1 до 7'))

print(check_day_off(input_number))
