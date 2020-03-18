import string_calculator
def test_empty_string():
    """adds an empty string in the add function in string_calculator"""
    assert string_calculator.add("") == 0

def test_one_string():
    """recives a string of a number and returns it as an integer"""
    assert string_calculator.add("465") == 465

def test_two_num_string():
    """supports two numbers"""
    assert string_calculator.add("1,2") == 3

def test_three_num_string():
    assert string_calculator.add("1,2,3") == 6

def test_much_unknown_argument():
    assert string_calculator.add("1,2,3,4,5,6,8,9,10,465") == 513