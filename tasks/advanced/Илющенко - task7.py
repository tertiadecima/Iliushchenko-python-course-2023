from collections import defaultdict, Counter
import pydot


def build_graph(words, mismatch_percent):
    graph = defaultdict(list)

    for i, word1 in enumerate(words):
        if i not in graph:
            graph[i] = []
        for j, word2 in enumerate(words[i+1:]): # переписать через индексы
            difference = 0

            if len(word1) != len(word2):
                continue

            for symbol1, symbol2 in zip(word1, word2):
                if symbol1 != symbol2:
                    difference += 1

            if difference < (mismatch_percent * len(word1) / 100):
                graph[i].append(j+1)
                graph[j+1].append(i)

    return graph


# words = ["hello", "helol", "ehllo", "tiger", "field"]
# g = build_graph(words, mismatch_percent=50.)
# print(dict(g))


def export_graph(graph, labels):
    graph_dot = pydot.Dot("", graph_type="graph")
    for key, value in graph.items():
        graph_dot.add_node(pydot.Node(key, label=labels[key]))
        for element in value:
            if element < key:
                pass
            else:
                graph_dot.add_edge(pydot.Edge(key, element))

    return graph_dot


# g = {0: [1, 2], 1: [0], 2: [0]}
# labels = ["a", "b", "c"]
# print(export_graph(g, labels))


def build_comp(node, graph, visited):
    work_list = [node]
    comp_conn = set()
    while work_list:
        node = work_list.pop(0)
        comp_conn.add(node)
        work_list.extend([element for element in graph[node] if element > node])
        visited.append(node)
    return comp_conn


def find_connected_components(graph):
    visited = []
    connected_components = []
    for key in graph:
        if key not in visited:
            conn_comp = build_comp(key, graph, visited)
            connected_components.append(conn_comp)
    return connected_components


# g = {0: [1, 2], 1: [0], 2: [0], 3: [], 4: []} # [{0, 1, 2}, {3}, {4}]
# g = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1], 4: []} # [{0, 1, 2, 3}, {4}]
# g = {0: [1], 1: [0, 3], 2: [5], 3: [1, 4, 6], 4: [3], 5:[2], 6:[3]} # [{0, 1, 3, 4, 6}, {2, 5}]
# print(find_connected_components(g))


def find_consensus(list_of_words):
    consensus_string = ''
    letters = defaultdict(list)
    for word in list_of_words:
        for place, letter in enumerate(word):
            letters[place].append(letter)
    for element in letters.values():
        consensus_string += Counter(element).most_common(1)[0][0]
    return consensus_string


print(find_consensus(["hello", "helol", "ehllo"])) # hello
print(find_consensus(["bug", "bow", "bag", "bar"])) # bag


def corrent_typos(list_of_words, mismatch_percent):
    graph = build_graph(list_of_words, mismatch_percent)
    # print('graph', dict(graph))
    # exported_graph = export_graph(graph, list_of_words)
    # print('exported_graph', exported_graph)
    components = find_connected_components(graph)
    # print('components', components)

    correct_list = []
    for num, connected in enumerate(components):
        if len(connected) > 1:
            list = [list_of_words[item] for item in connected]
            correct_word = find_consensus(list)
            for _ in range(len(connected)):
                correct_list.append(correct_word)
        else:
            correct_list.append(list_of_words[connected.pop()])
    return correct_list


words = ["hello", "helol", "ehllo", "tiger", "field", "abracadabra"]
print(corrent_typos(words, mismatch_percent=50.)) # ['hello', 'hello', 'hello', 'tiger', 'field', 'abracadabra']
