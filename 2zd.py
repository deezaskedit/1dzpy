# Задача 2. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inp_num(x):
    points = ['X', 'Y', 'Z']
    array = []
    for i in range(x):
        while True:
            try:
                array.append(int(input(f'Введите значение {points[i]}: ')))
                break
            except:
                print('Неправильный ввод, попробуйте снова ')
    return array


def predic(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    res = left == right
    return res


number = inp_num(3)

if predic(number) == True:
    print('Утверждение истинно:)')
else:
    print('Утверждение ложно:(')