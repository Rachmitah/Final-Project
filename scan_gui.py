import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import Axes3D

class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QPushButton('Start Scan')
        self.button.clicked.connect(self.plot)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self):
        data = [random.random() for i in range(10)]
        x1 = np.arange(0,20,1)
        y1 = np.arange(0,10,1)
        xs1, ys1 = np.meshgrid(x1, y1)
        zz1 = np.array([
            [random.random(), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 2, 2, 2, 1, random.random(), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 2, 2, 2, 1, 0, 0, 0, 0, random.random(), 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 2, 4, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 2, 3, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, random.random(), 0, 0, -(random.random()), 0],
            [0, 0, 1, 2, 3, 1, 1, 0, -(random.random()), 0, 0, 0, 0, 0, 0, 0, 0, 0, random.random(), 0],
            [0, 0, 1, 2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, random.random(), 0, 0, 0, 0, 0, 0]])

        self.figure.clear()
        #ax = self.figure.add_subplot(111)
        #ax.plot(data, '*-')
        

        ax = Axes3D(self.figure)
        ax.plot_surface(xs1, ys1, zz1, rstride=1, cstride=1, cmap=cm.coolwarm)
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = Window()
    main.show()

    sys.exit(app.exec_())
