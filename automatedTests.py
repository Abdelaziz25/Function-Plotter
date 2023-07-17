import pytest
from PySide2.QtTest import QTest
from PySide2.QtCore import Qt
from UserInputValidator import InputValidator
from PySide2.QtWidgets import QApplication,QMessageBox
from functionplot import FunctionPlotterApp

@pytest.fixture(scope="module")
def app():
    qapp = QApplication([])
    yield qapp
    qapp.quit()

def test_plot_function(app):
    function_plotter_app = FunctionPlotterApp()
    function_plotter_app.show()

    # Test 1: Valid function and range
    function_plotter_app.function_input.setText("x**2 + 3*x - 5")
    function_plotter_app.min_input.setText("-10")
    function_plotter_app.max_input.setText("10")
    QTest.mouseClick(function_plotter_app.plot_button, Qt.LeftButton)
    assert len(function_plotter_app.canvas.figure.get_axes()) == 1
    assert function_plotter_app.canvas.figure.get_axes()[0].get_title() == "Function Plot"




def test_validate_min_max():
    # Test 1: Valid minimum and maximum values
    assert InputValidator.validate_min_max(0, 10) is True

    # Test 2: Invalid minimum value equal to maximum value
    assert InputValidator.validate_min_max(5, 5) is False

    # Test 3: Invalid minimum value greater than maximum value
    assert InputValidator.validate_min_max(10, 5) is False


def test_validate_function():
    # Test 1: Valid function
    assert InputValidator.validate_function('2*x^2 + 3') is True

    # Test 2: Invalid function with an invalid character
    assert InputValidator.validate_function('2*x^2 + $') is False

    # Test 3: Invalid function with multiple invalid characters
    assert InputValidator.validate_function('2*x^2 + $%') is False


if __name__ == '__main__':
    pytest.main()
