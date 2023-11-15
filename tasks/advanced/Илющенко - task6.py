# Следующие задания нужно реализовать с помощью коллекций из модуля `collections`.
from collections import namedtuple
from collections import defaultdict

# 1. Factor (2 балла)
# Реализуйте функцию `factor`, которая строит сжатое представление
# последовательности с повторяющимися элементами. Результат вызова функции --
# именованный кортеж `Factor` с двумя полями `elements` и `levels`, где `levels`
# -- словарь, сопоставляющий каждому **уникальному** элементу входной
# последовательности его номер, а `elements` -- последовательность, кодирующая
# исходную при помощи номеров уникальных элементов.


# def factor(entry):
#     Factor = namedtuple('Factor', "elements levels")
#     num = 0
#     levels = {}
#     elements = []
#     for i in entry:
#         if i not in levels:
#             levels[i] = num
#             elements.append(num)
#             num += 1
#         else:
#             elements.append(levels[i])
#     f = Factor(elements = elements, levels = levels)
#     return f
#
#
# f = factor(["a", "a", "b"])
# print(f.elements)  # [0, 0, 1]
# print(f.levels["b"])  # 1
# print(list(f.levels.items()))  # [('a', 0), ('b', 1)]
#
# f = factor(["a", "b", "c", "b", "a"])
# print(f.elements)  # [0, 1, 2, 1, 0]
# print(list(f.levels.items()))  # [('a', 0), ('b', 1), ('c', 2)]

# Номера уровней в возвращаемом кортеже должны соответствовать порядку уникальных
# элементов во входном списке.

# 2. Group_by (2 балла)
# Реализуйте функцию `group_by`, группирующую переданную ей
# последовательность объектов по функции-ключу. Результатом функции `group_by`
# является словарь, в котором по ключу `k` содержится список объектов, на которых
# функция-ключ вернула значение `k`.


def group_by(objects, key):
    grouped_objs = defaultdict(list)
    for object in objects:
        grouped_objs[key(object)].append(object)
    return grouped_objs

print(dict(group_by(["foo", "foo", "barbra"], len)))  # {3: ['foo', 'boo'], 6: ['barbra']}

# 3. Invert (2 балла)
# Напишите функцию `invert`. Функция принимает словарь и возвращает новый
# словарь, в котором для каждого значения из исходного словаря содержится
# множество соответствующих ему ключей.


def invert(entry_dict):
    inverted_dict = defaultdict(set)
    for key, value in entry_dict.items():
        inverted_dict[value].add(key)
    return inverted_dict


print(dict(invert({"d": "a", "a": "42", "b": "42", "c": "24", })))  # {24: {'c'}, 42: {'b', 'a'}}
