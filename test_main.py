import main 

DataIn = ["0 0 1 0 0", "0 1 4 5 0", "0 5 5 6 1", "0 6 6 3 2", "1 0 1 2 2"]
DataLen = 5

def test_parse_input ():
    array = main.parse_input(DataIn)
    length = DataLen
    assert (len(array) == length)