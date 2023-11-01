import random
from collections import defaultdict


def words(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        raw = f.readlines()
        [line.split(" ").flatten() for line in f.readlines()]
    word_list = []
    # word_list.extend([line.split(' ') for line in raw])
    for line in raw:
        word_list.extend(line.split(' '))
    return (word_list)


# words = words('snoopdogg.txt')[:100]
# print(words)

def transition_matrix(words):
    matrix_dict = defaultdict(list)
    for i in range(len(words) - 2):
        pair = (words[i], words[i + 1])
        # if pair not in matrix_dict:
        #     matrix_dict[pair] = []
        # matrix_dict[pair].append(words[i + 2])
        matrix_dict[pair].append(words[i + 2])
    return matrix_dict


# matrix = transition_matrix(words)
# print(matrix)

def markov_chain(words, matrix, sent_len):
    pair = tuple(random.choices(words, k=2))
    sentence = pair[0] + ' ' + pair[1]
    for _ in range(sent_len - 2):
        if pair in matrix.keys():
            new_word = random.choice(matrix[pair])
        else:
            new_word = random.choice(words)
        sentence += ' ' + new_word
        pair = (pair[1], new_word)
    return sentence


# print(markov_chain(words, matrix, 10))

def snoop_says(file_name, sent_len):
    wordlist = words(file_name)
    matrix = transition_matrix(wordlist)
    return markov_chain(wordlist, matrix, sent_len)


print(snoop_says('snoopdogg.txt', 50))
