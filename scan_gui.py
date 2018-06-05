import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import time
usleep = lambda x: time.sleep(x/1000000.0)
import random
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import Axes3D
# from ultra_man import get_range

class Window(QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.button = QPushButton('Start Scan')
        self.button.clicked.connect(self.plot)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self):
        n    = 1
        posY = 0
        posX = 0
        x1 = np.arange(0,20,1)
        y1 = np.arange(0,10,1)
        xs1, ys1 = np.meshgrid(x1, y1)
        zz1 = np.array([
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

        for y in zz1:
            # Y Ganjil -> dari kiri ke kanan
            if (n == 1):
                posX = 0
                for x in y:
                        # lakukan scan ultrasonic
                        zz1[posY][posX] = posX
                        print(zz1[posY][posX])
                        posX += 1
                        self.figure.clear()        
                        ax = Axes3D(self.figure)
                        ax.plot_surface(xs1, ys1, zz1, rstride=1, cstride=1, cmap=cm.coolwarm)
                        self.canvas.draw()
                        self.canvas.flush_events()
                        
                n = 0
            # Y Genap -> dari kanan ke kiri
            else:
                posX -= 1
                for x in reversed(y):
                        # lakukan scan ultrasonic
                        zz1[posY][posX] = posX
                        print(zz1[posY][posX])
                        posX -= 1
                        self.figure.clear()        
                        ax = Axes3D(self.figure)
                        ax.plot_surface(xs1, ys1, zz1, rstride=1, cstride=1, cmap=cm.coolwarm)
                        self.canvas.draw()
                        self.canvas.flush_events()
                n = 1
            posY += 1
        print(zz1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())
