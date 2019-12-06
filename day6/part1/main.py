from utils import read_input, write_output, check_result
import re


def find_path(graph, node1, node2, path=[]):
    if node1 == "COM":
        return path

    for key in graph:
        if node1 in graph[key]:
            path.append(key)
            find_path(graph, key, node2, path)

    return path


def populate_graph(graph, node1, node2):
    if node1 in graph.keys():
        graph[node1].append(node2)
    else:
        graph[node1] = [node2]
    return graph


def calc(lines):
    result = 0
    parser = re.compile("[A-Z0-9]+")
    values = [tuple(parser.findall(line.strip())) for line in lines]
    graph = {}
    nodes = []

    for value in values:
        nodes.append(value[1])
        graph = populate_graph(graph, value[0], value[1])

    for node in nodes:
        path = find_path(graph, node, "COM", [])
        result += len(path)

    return result


if __name__ == '__main__':
    lines = read_input()
    result = str(calc(lines))
    write_output(result)
    check_result(result)
