import string_calculator
def test_empty_string():
    """adds an empty string in the add function in string_calculator"""
    assert string_calculator.add("") == 0

def test_one_string():
    """adds a string that is '1' and puts it in the add function in string_calculator"""
    assert string_calculator.add("1") == 1