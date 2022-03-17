# By Pytel & Karel
import sys

# ENUM
CLOSED = 0
UNVISITED = 1
OPENED = 2

def print_array (array):
    for line in array:
        print(line)

def parse_input (text):
    array = []
    for line in text:
        row = list(map(int, line.split()))
        array.append(row)
    return array

def read_input ():
    n = int(sys.stdin.readline())
    lines = sys.stdin.readlines()
    array = parse_input(lines)
    print_array(array)    
    assert(len(array) == n)
    return array

def make_array (X, Y, value):
    array = []
    for y in range(Y):
        row = []
        for x in range(X):
            row.append(value)
        array.append(row)
    return array

def empty (array):
    return len(array) == 0

def change_state (array, coord, state):
    X = len(array[0])
    Y = len(array)
    x, y = coord
    array[y][x] = state

def is_valid_coord(X,Y, x,y):
    return x >= 0 and x < X and y >= 0 and y < Y

def in_reach (value1, value2, dist):
    return abs(value2-value1) <= dist

def get_neaighbours_in_reach (array, coord, dist):
    X = len(array[0])
    Y = len(array)
    x, y = coord
    value = array[y][x]
    neighbors = []
    for vector in [[-1,0], [0,1], [+1,0], [0,-1]]:
    #for vector in [[-1,0], [-1,1], [0,1], [1,1], [+1,0], [+1,-1], [0,-1], [-1,-1]]:
        yd, xd = vector
        yn = y+yd
        xn = x+xd
        if is_valid_coord(X,Y, xn,yn) and in_reach(value, array[yn][xn], dist):
            neighbors.append([xn, yn])
    return neighbors

def in_state (array, coord, state):
    x, y = coord
    return array[y][x] == state

def solve(array, seed, dist):
    X = len(array[0])
    Y = len(array)

    solution = make_array(X, Y, UNVISITED)
    
    # init
    opened = [seed]
    change_state(solution, seed, OPENED)

    # iterate
    while not empty(opened):
        coord = opened.pop(0)
        to_open = get_neaighbours_in_reach(array, coord, dist)
        for new_coord in to_open:
            if not in_state(solution, new_coord, UNVISITED):
                continue
            change_state(solution, new_coord, OPENED)
            opened.append(new_coord)
        change_state(solution, coord, CLOSED)
    return solution

if __name__ == '__main__':
    array = read_input()
    dist = 2
    seed = [0,0]
    solution = solve(array, seed, dist)
    print_array(solution)

