import main
import pytest

# print_input bez testu
# read_input bez testu


@pytest.mark.parametrize('DataIn, DataLen', [
    (["0 0 1 0 0", "0 1 4 5 0", "0 5 5 6 1", "0 6 6 3 2", "1 0 1 2 2"], 5),
])
def test_parse_input(DataIn, DataLen):
    array = main.parse_input(DataIn)
    length = DataLen
    assert len(array) == length


@pytest.mark.parametrize('X, Y, value, validate', [
    (4, 3, 8, [[8, 8, 8, 8], [8, 8, 8, 8], [8, 8, 8, 8]]),
    (2, 3, 7, [[7, 7], [7, 7], [7, 7]]),
    (2, 2, 6, [[6, 6], [6, 6]]),
    (1, 1, 5, [[5]])
])
def test_make_array(X, Y, value, validate):
    assert main.make_array(X, Y, value) == validate


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

@pytest.mark.parametrize('value1, value2, max_distance, validate', [
    (4, 5, 0, False),
    (4, 5, 1, False),
    (4, 5, 2, True),
    (4, 5, 7, True),
    (2, 9, 8, True),
    (2, 9, 1, False)
])
def test_in_reach(value1, value2, max_distance, validate):
    assert main.in_reach(value1, value2, max_distance) == validate
