import pytest
from UserInput import UserInput
from UserInputValidator import InputValidator


def test_get_function(monkeypatch):
    # Simulate user input for the function
    monkeypatch.setattr('builtins.input', lambda _: '2*x^2 + 3')

    # Call the get_function method
    function = UserInput.get_function()

    # Check if the returned function matches the expected value
    assert function == '2*x^2 + 3'

    monkeypatch.setattr('builtins.input', lambda _: '2*x%2 + 3')

    # Call the get_function method
    function = UserInput.get_function()

    # Check if the returned function matches the expected value
    assert function == False


def test_validate_min_max():
    # Test valid minimum and maximum values
    min_value = 0
    max_value = 10
    assert InputValidator.validate_min_max(min_value, max_value) is True

    # Test minimum value equal to maximum value
    min_value = 5
    max_value = 5
    assert InputValidator.validate_min_max(min_value, max_value) is False

    # Test minimum value greater than maximum value
    min_value = 10
    max_value = 5
    assert InputValidator.validate_min_max(min_value, max_value) is False

def test_validate_function():
    # Test a valid function
    function = '2*x^2 + 3'
    assert InputValidator.validate_function(function) is True

    # Test an invalid function with an invalid character
    function = '2*x^2 + $'
    assert InputValidator.validate_function(function) is False

    # Test an invalid function with multiple invalid characters
    function = '2*x^2 + $%'
    assert InputValidator.validate_function(function) is False


if __name__ == '__main__':
    pytest.main()