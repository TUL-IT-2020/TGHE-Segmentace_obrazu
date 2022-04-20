import main

DataIn = ["0 0 1 0 0", "0 1 4 5 0", "0 5 5 6 1", "0 6 6 3 2", "1 0 1 2 2"]
DataLen = 5

# print_input bez testu
# read_input bez testu
#


def test_parse_input():
    array = main.parse_input(DataIn)
    length = DataLen
    assert len(array) == length


def test_make_array():
    assert main.make_array(4, 3, 8) == [[8, 8, 8, 8], [8, 8, 8, 8], [8, 8, 8, 8]]
    assert main.make_array(2, 3, 7) == [[7, 7], [7, 7], [7, 7]]
    assert main.make_array(2, 2, 6) == [[6, 6], [6, 6]]
    assert main.make_array(1, 1, 5) == [[5]]


def test_empty():
    assert main.empty([]) == True
    assert main.empty([1, 1]) == False


def test_is_valid_coord():
    assert main.is_valid_coord(4, 4, 2, 2) == True
    assert main.is_valid_coord(4, 4, 4, 4) == False
    assert main.is_valid_coord(4, 4, 5, 1) == False
    assert main.is_valid_coord(4, 4, 0, 0) == True
    assert main.is_valid_coord(4, 4, -0, +0) == True
    assert main.is_valid_coord(4, 4, -1, 2) == False


# in_state bez testu
# change_state bez testu


def test_in_reach():
    assert main.in_reach(4, 5, 0) == False
    assert main.in_reach(4, 5, 1) == True
    assert main.in_reach(4, 5, 2) == True
    assert main.in_reach(4, 5, 7) == True
    assert main.in_reach(2, 9, 8) == True
    assert main.in_reach(2, 9, 1) == False
