### 1. Parse_shebang (3 балла)
# [She-bang](http://en.wikipedia.org/wiki/Shebang_(Unix)) -- последовательность
# `#!`, которая используется для запуска исполняемых
# скриптов. She-bang пишется в самом начале файла. После него следует
# опциональный пробел и путь к программе, которая будет исполнять скрипт, например: #! /bin/sh, #!/usr/bin/env python3 -v
# Напишите функцию `parse_shebang`, которая принимает путь к скрипту
# и возвращает путь к программе, которая будет его исполнять, если скрипт содержит she-bang, и None` в обратном случае.


def parse_shebang(str):
    if str.startswith('#!'):
        path = str[2:].strip()
        if path.endswith('.txt'):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.readlines()
                return content
        return path
    else:
        return None


print(parse_shebang("#! /bin/sh"))  # "/bin/sh"
print(parse_shebang("#!/usr/bin/env python3 -v"))  # "/usr/bin/env python3 -v"
print(parse_shebang("#! task4.txt"))

# В следующих заданиях необходимо использовать методы класса `str` из лекции
### 2. Capwords (3 балла)
# Напишите функцию `capwords`, которая принимает строку и опциональный
# разделитель и возвращает новую строку, в которой каждое слово начинается с
# заглавной буквы. Логика работы функции `capwords` должна быть аналогична методу
# `str.split`.


def capwords_with_split(string, sep='\n'):
    split_str = string.split(sep)
    new_string = ''
    if sep == '\n': sep = ' '
    for part in split_str[:-1]:
        new_string += part.strip().capitalize() + str(sep)
    return repr(new_string.strip())


print(capwords_with_split("foo,bar boo,", sep=","))  # 'Foo,Bar boo,'
print(capwords_with_split(" foo \nbar\n"))  # 'Foo Bar'
print(capwords_with_split("foo,bar boo,", sep=""))  # ValueError: empty separator

### 3. Find all (2 балла)
# Напишите функцию `find_all`, которая возвращает список индексов всех
# вхождений подстроки в строке.

def find_all(str, substr):
    indexes = []
    start = 0
    while str.find(substr, start) != -1:
        substr_index = str.find(substr, start)
        indexes.append(substr_index)
        # if substr_index == 0:
        start = substr_index + len(substr)
        # else:
        #     start += len(substr)
    return indexes


print(find_all("abcdaa", "a"))  # [0, 4, 5]

### 4. Common prefix (2 балла)
# Напишите функцию `common_prefix`, которая возвращает наибольший общий
# префикс двух или более строк.


def common_prefix_initial(*args):
    assert args, 'No args!'
    arr = args
    arg_len = len(arr)
    min_len = len(arr[0])

    for i in range(1, arg_len):
        if (len(arr[i]) < min_len):
            min_len = len(arr[i])

    prefix = ""
    for i in range(min_len):
        current = arr[0][i]

        for j in range(1, arg_len):
            if (arr[j][i] != current):
                return prefix

        prefix = prefix + current

    return prefix


def common_prefix(*args):
    word0 = args[0]
    length = len(word0)
    for i in range(1, len(args)):
        word = args[i]
        length = min(length, len(word))  # длина самого короткого слова

        for i in range(length):
            if word0[i] != word[i]:
                length = i
                break
    return word0[:length]


print(common_prefix("abcd", "foobar"))  # ""
print(common_prefix("foo", "foobar", "foil"))  # "fo"
print(common_prefix("foo", "foobar", "front", 'fooor'))  # "f"
print(common_prefix("foo", "foobar", "front", 'fr'))  # "f"
