import pytest
from PySide2 import QtCore
from PySide2.QtTest import QTest
from PySide2.QtCore import Qt
from UserInputValidator import InputValidator
from PySide2.QtWidgets import QApplication
from functionplot import FunctionPlotterApp

@pytest.fixture(scope="module")
def app():
    qapp = QApplication([])
    yield qapp
    qapp.quit()

def test_plot_function(app):
    function_plotter_app = FunctionPlotterApp()
    function_plotter_app.show()

    # Simulate user input
    function_plotter_app.function_input.setText("x**2 + 3*x - 5")
    function_plotter_app.min_input.setText("-10")
    function_plotter_app.max_input.setText("10")

    # Click the "Plot Function" button
    QTest.mouseClick(function_plotter_app.plot_button, Qt.LeftButton)

    # Get the plotted axes
    axes = function_plotter_app.canvas.figure.get_axes()

    # Assert that the plot is displayed correctly
    assert len(axes) == 1
    assert axes[0].get_title() == "Function Plot"


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