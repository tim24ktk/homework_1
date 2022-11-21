"""
Напишите программу для проверки истинности утверждения
 ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
  ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"
"""


def input_numbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def check_predicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = input_numbers(3)

if check_predicate(statement):
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
