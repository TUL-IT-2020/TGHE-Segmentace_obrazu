# By Pytel & KNajman
import sys
import heapq

DEBUG = False

# ENUM
OPENED = 0
VISITED = 1
BACKGROUND = OPENED

class Vertex():
    def __init__(self, value, coord):
        self.value = value
        self.coord = coord
    
    def __str__(self):
        return str(self.value) + ", " + str(self.coord)
    
    def __sub__(self, other):
        return abs(self.value - other.value)

class Edge():
    def __init__(self, vertex1, vertex2):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.value = vertex1 - vertex2

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return ("Value: " + str(self.value) + 
        ", vertex A: " + str(self.vertex1) + 
        ", vertex B: " + str(self.vertex2))

def print_array(array):
    for line in array:
        for value in line:
            print(value, end =" ")
        print("")

def parse_input(text):
    array = []
    for line in text:
        row = list(map(int, line.split()))
        array.append(row)
    return array

def read_input():
    n = int(sys.stdin.readline())
    lines = sys.stdin.readlines()
    array = parse_input(lines)
    if DEBUG: 
        print_array(array)
    assert len(array) == n
    return array

def make_array(X, Y, value):
    array = []
    for y in range(Y):
        row = []
        for x in range(X):
            row.append(value)
        array.append(row)
    return array

def empty(array):
    return len(array) == 0

def change_state(array, coordinations, state):
    x, y = coordinations
    array[y][x] = state

def is_valid_coord(X, Y, x, y):
    return X > x >= 0 and Y > y >= 0

def in_reach(value1, value2, max_distance):
    return abs(value2 - value1) <= max_distance

def visited(value):
    return value == VISITED

def add_neaighbours(array, coord, heap):
    X = len(array[0])
    Y = len(array)
    x, y = coord
    value = array[y][x]
    vertex1 = Vertex(value, coord)
    for vector in [[-1, 0], [0, 1], [+1, 0], [0, -1]]:
    # for vector in [[-1,0], [-1,1], [0,1], [1,1], [+1,0], [+1,-1], [0,-1], [-1,-1]]:
        yd, xd = vector
        yn = y + yd
        xn = x + xd
        if is_valid_coord(X, Y, xn, yn):
            vertex2 = Vertex(array[yn][xn], [xn, yn])
            edge = Edge(vertex1, vertex2)
            heapq.heappush(heap, edge)

def in_state(array, coord, state):
    x, y = coord
    return array[y][x] == state

def solve(values_array, seed):
    X = len(values_array[0])
    Y = len(values_array)

    visited_array = make_array(X, Y, OPENED)
    # init
    tree = []
    heap = []
    heapq.heapify(heap)
    change_state(visited_array, seed, VISITED)
    add_neaighbours(values_array, seed, heap)

    # iterate
    while not empty(heap):
        edge = heapq.heappop(heap)
        vertex = edge.vertex2
        coord = vertex.coord
        if not in_state(visited_array, coord, OPENED):
            continue
        change_state(visited_array, coord, VISITED)
        add_neaighbours(values_array, coord, heap)
        tree.append(edge)
        if DEBUG:
            print()
            print_array(visited_array)

    # split to backg/forg
    max_index, max_edge = max(enumerate(tree), key=lambda item: item[1].value)
    if DEBUG:
        print(max_index, max_edge)
    background = tree[0 : max_index]
    solution = visited_array
    change_state(solution, seed, BACKGROUND)
    for edge in background:
        coord = edge.vertex2.coord
        change_state(solution, coord, BACKGROUND)

    return solution

if __name__ == "__main__":
    values_array = read_input()
    seed = [0, 0]
    solution = solve(values_array, seed)
    print_array(solution)
