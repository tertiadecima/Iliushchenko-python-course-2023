def padded(iterator, default, length):
    iter_list = list(iterator)
    if len(iter_list) >= length:
        iter_list = iter_list[:length]
    else:
        while len(iter_list) < length:
            iter_list.append(default)
    # print(type(iter(iter_list)))
    return iter(iter_list)


print(list(padded(range(3), -42, 5)))  # [0, 1, 2, -42, -42]

print(list(padded(range(3), -42, 1)))  # [0]


def sliding(iterator, size, step):
    iter_list = list(iterator)
    curr_start = 0
    fin_list = []
    while curr_start < len(iterator) - size:
        fin_list.append(iter_list[curr_start:curr_start+size])
        curr_start += step
    return iter(fin_list)


print(list(map(list, sliding(range(10), 3, 2))))  # [[0, 1, 2], [2, 3, 4], [4, 5, 6], [6, 7, 8]]
