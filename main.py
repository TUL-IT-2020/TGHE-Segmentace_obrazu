# By Pytel & KNajman
import sys

# ENUM
CLOSED = 0
UNVISITED = 1
OPENED = 2


def print_array(array):
    for line in array:
        print(line)


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


def get_neaighbours_in_reach(array, coordinations, distance):
    X = len(array[0])
    Y = len(array)
    x, y = coordinations
    value = array[y][x]
    neighbors = []
    for vector in [[-1, 0], [0, 1], [+1, 0], [0, -1]]:
        # for vector in [[-1,0], [-1,1], [0,1], [1,1], [+1,0], [+1,-1], [0,-1], [-1,-1]]:
        yd, xd = vector
        yn = y + yd
        xn = x + xd
        if is_valid_coord(X, Y, xn, yn) and in_reach(value, array[yn][xn], distance):
            neighbors.append([xn, yn])
    return neighbors


def in_state(array, coord, state):
    x, y = coord
    return array[y][x] == state


def solve(array, seed, distance):
    X = len(array[0])
    Y = len(array)

    solution_array = make_array(X, Y, UNVISITED)
    # init
    opened = [seed]
    change_state(solution_array, seed, OPENED)

    # iterate
    while not empty(opened):
        coord = opened.pop(0)
        to_open = get_neaighbours_in_reach(array, coord, distance)
        for new_coord in to_open:
            if not in_state(solution_array, new_coord, UNVISITED):
                continue
            change_state(solution_array, new_coord, OPENED)
            opened.append(new_coord)
        change_state(solution_array, coord, CLOSED)
    return solution_array


if __name__ == "__main__":
    array = read_input()
    DISTANCE = 2
    seed = [0, 0]
    solution = solve(array, seed, DISTANCE)
    print_array(solution)
