
Function Plotter

The Function Plotter is a simple PyQt-based desktop application that allows users to plot mathematical functions and visualize their graphs. Users can input a mathematical function in terms of 'x' and specify the range of values for 'x' to be plotted. The application then generates and displays the corresponding graph.

# Requirements:
To run the Function Plotter application, you need the following:
Python (3.6 or later)
PyQt5 (PySide2)
NumPy
Matplotlib

# Installation:

Make sure you have Python installed on your system. If not, download and install it from the official Python website.

Install the required Python libraries using pip:
pip install pyqt5 numpy matplotlib

# Usage
Run the main.py file to launch the Function Plotter application.

python main.py


The application window will appear, prompting you to enter the function and the range of 'x' values.

Enter a valid mathematical function in the format accepted by the application, e.g., x^2 + 3*x - 5. Allowed characters are digits, 'x', '.', '+', '-', '*', '/', '^', and whitespaces.

Enter the minimum and maximum values for 'x' to define the range over which the function will be plotted.

Click the "Plot Function" button to generate and display the graph of the function within the specified range.


# Code Overview:

The code consists of three main files:

main.py: This is the entry point of the application. It sets up the PyQt application and initializes the FunctionPlotterApp.

functionplot.py: This file contains the FunctionPlotterApp class, which represents the main application window. It handles user inputs, validates them, and generates the function plot using NumPy and Matplotlib.

UserInputValidator.py: This file contains the InputValidator class, which provides validation functions for checking the user's input for the function and the range of values.

# Automated Testing:
The code also includes a set of automated tests to ensure the proper functionality of the application. These tests use the PyTest framework.

