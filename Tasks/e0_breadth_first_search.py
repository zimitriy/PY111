from collections import deque
from typing import Hashable, List

import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    for edge in graph.edges:
        nx.draw_networkx_edges(
            graph, pos,
            edgelist=[(edge[0], edge[1])], connectionstyle="arc3,rad=0.2"
        )

    plt.show()  # plt.savefig()


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order
    Выполняет поиск в ширину и возвращает список узлов в порядке посещения

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """

    draw_graph(g)

    path_nodes = []  # сгоревшие узлы в порядке их сгорания
    visited_nodes = {node: False for node in g.nodes}

    wait_nodes = deque()  # очередь из горящих узлов, ожидающих поджечь своих соседей
    wait_nodes.append(start_node)
    visited_nodes[start_node] = True

    while wait_nodes:
        current_node = wait_nodes.popleft()  # забираем горящий узел с начала очереди
        neighbours = g[current_node]

        for neighbour in neighbours:
            if not visited_nodes[neighbour]:
                wait_nodes.append(neighbour)  # конец очереди справа
                visited_nodes[neighbour] = True

        path_nodes.append(current_node)

    print(g, start_node)

    return path_nodes
