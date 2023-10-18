import functools

# 1. Union (2 балла)
# Используя оператор `|`, реализуйте функцию `union`, возвращающую
# объединение произвольного числа множеств. Если нужно, используйте функцию `functools.reduce`.


def union(first, *args):
    unionized_set = first
    for set in args:
        unionized_set |= set

    return unionized_set


print(union({'a', 'b', 'c', 'd', 'e'}, {'h', 'o', 'l', 'e'}, {1, 2, 3, 4, 5}))
print(functools.reduce(union, [{'a', 'b', 'c', 'd', 'e'}, {'h', 'o', 'l', 'e'}, {1, 2, 3, 4, 5}]))

# 2. Digits (2 балла)
# Реализуйте функцию `digits`, возвращающую список цифр неотрицательного
# целого числа. Если нужно, используйте функцию `functools.reduce`.


def digits(number):
    assert number >= 0 and type(number) is int
    if type(number) is not int:
        number = list(map(list, number.split(' ')))
    list_of_nums = []
    for el in str(number):
        list_of_nums.append(int(el))
    return list(list_of_nums)


# print(digits(-59))
print(digits(31415926))
print(digits(0))

# 3. Trace_if (4 балла)
# Измените декоратор `trace` из лекции, чтобы он выводил информацию о
# вызове функции, только если переданные аргументы удовлетворяют предикату.

from functools import wraps


def checker(predicate=lambda x: x>0):  # сам декоратор
    def decorate(f):
        @wraps(f)
        def wrapper(*args):  # передаем предикат и аргументы на проверку
            for element in args:
                if not predicate(element):
                    print("Doesn't satisfy the predicate")
                    return f(*args)
            else:
                call = ", ".join(
                    [str(a) for a in args]
                )
                print(f"{f.__name__}({call}) = ...")
                ret = f(*args)
                print(f"{f.__name__}({call}) = {ret}")
                return ret
        return wrapper
    return decorate


@checker(lambda x: x % 2 == 0)
def max(*args):  # рабочая ф-я под проверку
    ret = 0
    for x in args:
        ret = ret if x < ret else x
    return ret


print(max(4, 8, 24))
print(max(4, 9, 24))
# проверяем, что находим максимальное из положительных четных чисел

# 4. N_times (4 балла)
# Реализуйте декоратор `n_times`. Результатом его работы должна быть
# функцию, вызывающая декорируемую функцию `n` раз. Возвращаемое значение можно игнорировать.

from functools import wraps


def n_times(num):
    def decorate(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                f(*args, **kwargs)
        return wrapper
    return decorate


@n_times(3)
def hello():
    print('Hello world')


hello()
