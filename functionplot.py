import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from matplotlib.figure import Figure

from UserInputValidator import InputValidator

class FunctionPlotterApp(QMainWindow):
    def __init__(self):
        super(FunctionPlotterApp, self).__init__()
        self.setWindowTitle("Function Plotter")
        self.setGeometry(100, 100, 800, 600)

        # Set up the main central widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create input widgets and plot button
        self.function_label = QLabel("Enter function (e.g., x^2 + 3*x - 5): ")
        self.function_input = QLineEdit()
        self.min_label = QLabel("Enter min value: ")
        self.min_input = QLineEdit()
        self.max_label = QLabel("Enter max value: ")
        self.max_input = QLineEdit()
        self.plot_button = QPushButton("Plot Function")

        # Add input widgets and plot button to the layout
        self.layout.addWidget(self.function_label)
        self.layout.addWidget(self.function_input)
        self.layout.addWidget(self.min_label)
        self.layout.addWidget(self.min_input)
        self.layout.addWidget(self.max_label)
        self.layout.addWidget(self.max_input)
        self.layout.addWidget(self.plot_button)

        # Connect the "Plot Function" button to the plot function
        self.plot_button.clicked.connect(self.on_plot_button_clicked)

        # Initialize the canvas attribute for plotting
        self.canvas = FigureCanvas(Figure())
        self.layout.addWidget(self.canvas)

    def on_plot_button_clicked(self):
        # Get user input from input fields
        function_str = self.function_input.text()
        min_value_str = self.min_input.text()
        max_value_str = self.max_input.text()

        # Validate function and min/max values using the InputValidator class
        if not InputValidator.validate_function(function_str):
            self.show_error_message("Invalid characters in the function.")
            return
        try:
            min_value = float(min_value_str)
            max_value = float(max_value_str)
        except ValueError:
            self.show_error_message("Invalid min or max value. Please enter numeric values.")
            return

        if not InputValidator.validate_min_max(min_value, max_value):
            self.show_error_message("Invalid min or max value. Minimum value should be smaller than the maximum value.")
            return

        # Replace '^' with '**' for Python evaluation and remove any dots from the function
        function_str = function_str.replace('^', '**')
        function_str = function_str.replace('.', '')

        # Generate x and y values for the function to plot
        x = np.linspace(float(min_value_str), float(max_value_str), 100)
        y = [eval(function_str, {"x": i}) for i in x]

        # Clear any previous plots on the canvas
        self.canvas.figure.clear()

        # Create a new plot on the canvas
        ax = self.canvas.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Function Plot")

        # Draw the new plot on the canvas
        self.canvas.draw()

    def show_error_message(self, message):
        # Show an error message in a QMessageBox
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle("Error")
        error_box.setText(message)
        error_box.exec_()
