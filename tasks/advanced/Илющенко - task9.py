from itertools import count, cycle, islice


# def padded(iterator, default, length):
#     iter_list = list(iterator)
#     if len(iter_list) >= length:
#         iter_list = iter_list[:length]
#     else:
#         while len(iter_list) < length:
#             iter_list.append(default)
#     # print(type(iter(iter_list)))
#     return iter(iter_list)
#
def padded_2(iterator, default, n):
    iterator = iter(iterator)
    for _ in range(n):
        yield next(iterator, default)

print(list(padded_2(range(3), -42, 5)))  # [0, 1, 2, -42, -42]
print(list(padded_2(range(3), -42, 1)))  # [0]
print(list(padded_2(count(), -42, 30)))


class SmthWithIter:
    def __iter__(self):
        return Iter()

class Iter:
    def __init__(self):
        self.i = 0

    def __next__(self):
        if self.i > 10:
            raise StopIteration()
        self.i += 1
        return 1

print(list(padded_2(SmthWithIter(), -42, 30)))


def sliding(iterator, size, step):
    assert size >= step, "Block size should be greater than step size"
    iter_list = list(iterator)
    curr_start = 0
    fin_list = []
    while curr_start < len(iterator) - size:
        fin_list.append(iter_list[curr_start:curr_start + size])
        curr_start += step
    return iter(fin_list)


def sliding_2(iterator, n, step):
    assert n >= step, "Block size should be greater than step size"
    iterator_block = iter(iterator)

    block = []
    for _ in range(n):
        try:
            block.append(next(iterator_block))
        except StopIteration:
            return
    yield block
    while True:
        rest = block[n - step + 1:]
        for _ in range(n - len(rest)):
            try:
                rest.append(next(iterator_block))
            except StopIteration:
                return
        yield rest
        block = rest
        # for _ in range(step):
        #     try:
        #         a = next(iterator_step)
        #     except StopIteration:
        #         return
        # iterator_block = iterator_step



print(list(map(list, sliding_2(range(2), 3, 2))))  # [[0, 1, 2], [2, 3, 4], [4, 5, 6], [6, 7, 8]]
print(list(map(list, sliding_2(SmthWithIter(), 3, 2))))
# for block in sliding_2(count(), 3, 2):
#     print(block)
