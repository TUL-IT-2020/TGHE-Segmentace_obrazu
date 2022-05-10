# By Pytel & KNajman
"""
Řešení pro problém: Segmentace obrazu
"""
import sys
import heapq

DEBUG = False

# ENUM
OPENED = 0
VISITED = 1
BACKGROUND = OPENED


class Vertex:
    def __init__(self, value, coord):
        self.value = value
        self.coord = coord

    def __str__(self):
        return str(self.value) + ", " + str(self.coord)

    def __sub__(self, other):
        return abs(self.value - other.value)


class Edge:
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.value = vertex1 - vertex2

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return (
            "Value: "
            + str(self.value)
            + ", vertex A: "
            + str(self.vertex1)
            + ", vertex B: "
            + str(self.vertex2)
        )


def print_array(array):
    """
    print inputed array
    """
    for line in array:
        for value in line:
            print(value, end=" ")
        print("")


def parse_input(text):
    """
    parse input text to array
    """
    array = []
    for line in text:
        row = list(map(int, line.split()))
        array.append(row)
    return array


def read_input():
    """
    read input from stdin
    """
    n = int(sys.stdin.readline())
    lines = sys.stdin.readlines()
    array = parse_input(lines)
    if DEBUG:
        print_array(array)
    assert len(array) == n
    return array


def make_array(X, Y, value):
    """
    make array with given size and value
    """
    array = []
    for _ in range(Y):
        row = []
        for _ in range(X):
            row.append(value)
        array.append(row)
    return array


def empty(array):
    """
    return true if array is empty
    """
    return len(array) == 0


def change_state(array, coordinations, state):
    """
    change state for field of given coordinates
    """
    x, y = coordinations
    array[y][x] = state


def is_valid_coord(X, Y, x, y):
    """
    return true if coord is valid
    """
    return X > x >= 0 and Y > y >= 0


def in_reach(value1, value2, max_distance):
    """
    return true if value1 is in reach of value2
    """
    return abs(value2 - value1) < max_distance


def visited(value):
    """
    return true if value is visited
    """
    return value == VISITED


def add_neighbours(array, coord, heap):
    """
    add neaighbours to heap
    """
    X = len(array[0])
    Y = len(array)
    x, y = coord
    value = array[y][x]
    vertex1 = Vertex(value, coord)
    for vector in [[-1, 0], [0, 1], [+1, 0], [0, -1]]:
        # for vector in [[-1,0], [-1,1], [0,1], [1,1], [+1,0], [+1,-1], [0,-1], [-1,-1]]:
        y_d, x_d = vector
        y_n = y + y_d
        x_n = x + x_d
        if is_valid_coord(X, Y, x_n, y_n):
            vertex2 = Vertex(array[y_n][x_n], [x_n, y_n])
            edge = Edge(vertex1, vertex2)
            heapq.heappush(heap, edge)


def in_state(array, coord, state):
    """
    return true if coord is in state
    """
    x, y = coord
    return array[y][x] == state


def solve(values_array, seed):
    """
    return minumum spanning tree of the image
    """
    X = len(values_array[0])
    Y = len(values_array)

    visited_array = make_array(X, Y, OPENED)
    # init
    tree = []
    heap = []
    heapq.heapify(heap)
    change_state(visited_array, seed, VISITED)
    add_neighbours(values_array, seed, heap)

    # iterate
    while not empty(heap):
        edge = heapq.heappop(heap)
        vertex = edge.vertex2
        coord = vertex.coord
        if not in_state(visited_array, coord, OPENED):
            continue
        change_state(visited_array, coord, VISITED)
        add_neighbours(values_array, coord, heap)
        tree.append(edge)
        if DEBUG:
            print()
            print_array(visited_array)

    # split to backg/forg
    max_index, max_edge = max(enumerate(tree), key=lambda item: item[1].value)
    if DEBUG:
        print(max_index, max_edge)
    background = tree[0:max_index]
    solution = visited_array
    change_state(solution, seed, BACKGROUND)
    for edge in background:
        coord = edge.vertex2.coord
        change_state(solution, coord, BACKGROUND)

    return solution


if __name__ == "__main__":
    values_array = read_input()
    solution = solve(values_array, [0, 0])
    print_array(solution)
