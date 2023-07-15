import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from matplotlib.figure import Figure

from UserInputValidator import InputValidator

class FunctionPlotterApp(QMainWindow):
    def __init__(self):
        super(FunctionPlotterApp, self).__init__()
        self.setWindowTitle("Function Plotter")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.function_label = QLabel("Enter function (e.g., 'x^2 + 3*x - 5'): ")
        self.function_input = QLineEdit()
        self.min_label = QLabel("Enter min value: ")
        self.min_input = QLineEdit()
        self.max_label = QLabel("Enter max value: ")
        self.max_input = QLineEdit()
        self.plot_button = QPushButton("Plot Function")

        self.layout.addWidget(self.function_label)
        self.layout.addWidget(self.function_input)
        self.layout.addWidget(self.min_label)
        self.layout.addWidget(self.min_input)
        self.layout.addWidget(self.max_label)
        self.layout.addWidget(self.max_input)
        self.layout.addWidget(self.plot_button)

        self.plot_button.clicked.connect(self.on_plot_button_clicked)

        # Initialize the canvas attribute
        self.canvas = FigureCanvas(Figure())
        self.layout.addWidget(self.canvas)
    def on_plot_button_clicked(self):
        function_str = self.function_input.text()
        min_value_str = self.min_input.text()
        max_value_str = self.max_input.text()

        # Validate function and min/max values
        if not InputValidator.validate_function(function_str) or \
           not InputValidator.validate_min_max(float(min_value_str), float(max_value_str)):
            return
        function_str = function_str.replace('^', '**')
        function_str = function_str.replace('.', '')
        x = np.linspace(float(min_value_str), float(max_value_str), 100)
        y = [eval(function_str, {"x": i}) for i in x]

        # Clear any previous plots
        self.canvas.figure.clear()


        # Create a new plot
        ax = self.canvas.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Function Plot")

        # Draw the new plot
        self.canvas.draw()