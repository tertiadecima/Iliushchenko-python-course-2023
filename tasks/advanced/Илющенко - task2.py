# 1. Compose (3 балла)
# Напишите функцию `compose`, которая строит
# композицию двух переданных ей функций (сначала применяется правая функция, потом левая).
# Можно воспользоваться анонимными функциями (лямбдами) для построения.

def compose(fun1, fun2):
    return lambda *args: fun1(fun2(*args))


f = compose(lambda x: x * x, lambda x, y, z: x + y + z)
print(f(2, 2, 2))

# 2. Curry (5 баллов)
# Напишите функцию `curry`, которая принимает функцию `f`. `curry` должна
# возвращать новую функцию, у которой часть аргументов зафиксирована. Эти
# аргументы также должны быть переданы в функцию `curry`.
# Можно воспользоваться анонимными функциями (лямбдами) для построения.


def curry(fun, *fixed_args):
    return lambda arg: fun(arg, *fixed_args)


def add(x, y, z):
    return x + y + z


add_ten = curry(add, 10, 20)
print(add_ten(42))  # 52


# 3. Any (2 балла)
# Напишите функцию `any`, которая по переданному предикату
# и последовательности проверяет, что есть хотя бы один
# элемент последовательности, который удовлетворяет предикату.


def any(check, array):
    for element in array:
        if check(element):
            return True
    else:
        return False


print(any(lambda x: x % 2 == 0, [4, 9, 15]))  # True
# аттрибуты лямбды

# 4. All (2 балла)
# Напишите функцию `all`, которая по переданному предикату
# и последовательности проверяет, что все элементы
# последовательности удовлетворяют предикату.


def all(check, array):
    assert isinstance(array, list)
    for element in array:
        if not check(element):
            return False
    else:
        return True


print(all(lambda x: x % 2 == 0, [4, 8]))  # False
# for-else
