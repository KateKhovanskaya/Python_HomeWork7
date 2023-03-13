# Задача 36: На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N',
# 'значение_N'))
# Выводить на экран получившийся кортеж.
# Sample Input:
# house=дом car=машина men=человек tree=дерево
# Sample Output:
# ((house, дом), (car, машина), (men, человек), (tree, дерево))


def make_tuple(out_str):
    return tuple(out_str.split('='))


output_str = "house=дом car=машина men=человек tree=дерево"
output_str = tuple(map(make_tuple, output_str.split()))
print(output_str)