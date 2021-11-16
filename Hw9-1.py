# 1
"""Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков."""
"""a = ["Ivan", "Kolya", "Sergey", "Nikolas", "Lion", "Man"]
flip = list(map(lambda x: a.index(x), a))
rez = (map(lambda x, y: f'{x}-{y}', a, flip))
new_a = [rez for rez in rez]
print(new_a)"""


"""Создать lambda функцию, которая принимает на вход неопределенное
количество именных аргументов и выводит словарь с ключами удвоенной
длины.{‘abc’: 5} -> {‘abcabc’: 5}"""

"""lambda **kwargs: {k*2: value for k, value in kwargs.items()}"""

"""Создать декоратор для функции которая принимает список чисел. 
Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка"""


# 3 каким образом мы получаем числа в переменную а
"""def my_decorator(func):
    def wrapper(a):
        new_a = [i for i in a if i % 2]
        return func(new_a)

    return wrapper


@my_decorator
def real_func(x):
    print(x)


real_func([1, 2, 3, 4, 5, 8, ])"""
# 4
"""my_list = [1, 2, 3, 4, 5, 6, 7, 8]


def my_decorator_universal(func):
    def xz_universal(*args):
        return func(my_list[::-1])
    return xz_universal


@my_decorator_universal
def my_func(numbers: list):
    print(numbers)


my_func(my_list)"""
