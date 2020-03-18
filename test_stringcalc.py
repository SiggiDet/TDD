import string_calculator
def test_empty_string():
    """adds an empty string in the add function in string_calculator"""
    assert string_calculator.add("") == 0

def test_one_string():
    """recives a string of a number and returns it as an integer"""

    assert string_calculator.add("465") == 465