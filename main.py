import sys
from PySide2.QtWidgets import QApplication
from functionplot import FunctionPlotterApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FunctionPlotterApp()
    window.show()
    sys.exit(app.exec_())



