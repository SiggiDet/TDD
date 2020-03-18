import string_calculator
def test_empty_string():
    """recieves an empty string and puts it in the add function in string_calculator"""
    assert string_calculator.add("") == 0