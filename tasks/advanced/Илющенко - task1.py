# 1. Поиск уникальных слов (2 балла)
# Напишите функцию n_unique_words, которая:
# принимает на вход строку
# разбивает ее по пробелам на слова
# считает, сколько уникальных слов встретилось в строке
# Алгоритмическая сложность функции - О(n)
import sys


def n_unique_words(raw_string):
    str_arr = raw_string.split()
    print(str_arr)
    unique_objs = set(str_arr)
    print(unique_objs)
    return len(unique_objs)


print(n_unique_words('Моя мама была мама и она всегда мама рама была около вчера дорога и красива'))

# 2. Римские числа (5 баллов)
# Напишите функцию from_roman, которая:
# принимает на вход строку, которое содержит римское число
# в качестве результата возвращает целое число - результат перевода в арабские цифры


def from_roman(roman_str):
    complex = {'IV': 4, 'IX': 9, "XL": 40, 'XC': 90, 'CD': 400, 'CM': 900}
    simple = {"*": 0, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    number = 0
    for i in range(len(roman_str)-1):
        pair = roman_str[i:i+2]
        if pair in complex:
            roman_str = roman_str.replace(pair, '*')
            number += complex[pair]
    for i in range(len(roman_str)):
        number += simple[roman_str[i]]
    return number


def from_roman_2(roman_str):
    assert roman_str, 'Change the number'
    simple = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    prev = simple[roman_str[0]]
    curr = 0
    for roman_digit in roman_str[1:]:
        curr = simple[roman_digit]
        if prev < curr:
            number -= prev
        else:
            number += prev
        prev = curr
    number += curr
    return number


print(from_roman_2('XLVIII'))  # 48
print(from_roman_2('XCIX'))  # 99
print(from_roman_2('XCV'))  # 95
print(from_roman_2('DCCCXV'))  # 815
print(from_roman_2('MCMLXXXIV'))  # 1984
print(from_roman_2('XIV'))  # 14

# 3. Автодополнение (3 балла)
# Напишите функцию completion, которая:
# принимает на вход слово (то, что напечатал пользователь) и список слов (возможные варианты)
# в заданном списке нужно найти все слова, которые:
# начинаются также, как слово пользователя (без учета регистра)
# больше или равны по длине чем данное слово
# в качестве результата функции нужно напечатать список подходящих слов по длине
# (от самого короткого до самого длинного, если слова одинаковой длины, то порядок не важен)


def completion(word, possible_vars):
    assert word, 'Your word is empty'
    checked = []
    word_low = word.lower()
    for variant in possible_vars:
        if variant.lower().startswith(word_low):
            checked.append(variant)
    return sorted(checked, key=len)


word = input('Input your word: ')
if len(word) > 0:
    print(completion(word, ['moms', 'drum', 'mom', 'mother', 'muggers', 'lamp', '', '42', 'mathematical', 'mundane']))
else:
    print('Enter non-empty word', file=sys.stderr)
