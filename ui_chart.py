from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class DependencyChart(FigureCanvas):
    def __init__(self):
        self.figure = Figure(figsize=(4, 3))
        super().__init__(self.figure)
        self.setup_chart()

    def setup_chart(self):
        self.ax = self.figure.add_subplot(111)
        self.ax.set_facecolor('#F5F5F5')
        self.figure.patch.set_alpha(0)

    def update_chart(self, graph_data: dict):
        self.ax.clear()
        
        # Chart drawing logic here
        self.draw()
