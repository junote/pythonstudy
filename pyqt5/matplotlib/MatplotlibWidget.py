import sys
import random
import matplotlib

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QSizePolicy, QWidget
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt




class MyMplCanvas(FigureCanvas):


    def __init__(self, parent=None, width=5, height=4, dpi=100):


        self.fig = Figure(figsize=(width, height), dpi=dpi)  
        self.axes = self.fig.add_subplot(111)  

        # self.axes.hold(False)  

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def start_static_plot(self):
        self.fig.suptitle('static')
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)
        self.axes.set_ylabel('Y')
        self.axes.set_xlabel('X')
        self.axes.grid(True)



    def start_dynamic_plot(self, *args, **kwargs):
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure) 
        timer.start(1000)  



    def update_figure(self):
        self.fig.suptitle('dynamic')
        l = [random.randint(0, 10) for i in range(4)]
        self.axes.plot([0, 1, 2, 3], l, 'r')
        self.axes.set_ylabel('Y')
        self.axes.set_xlabel('X')
        self.axes.grid(True)
        self.draw()


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.initUi()

    def initUi(self):
        self.layout = QVBoxLayout(self)
        self.mpl = MyMplCanvas(self, width=5, height=4, dpi=100)
        self.mpl_ntb = NavigationToolbar(self.mpl, self)

        self.layout.addWidget(self.mpl)
        self.layout.addWidget(self.mpl_ntb)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MatplotlibWidget()
    ui.mpl.start_static_plot() 
    # ui.mpl.start_dynamic_plot()
    ui.show()
    sys.exit(app.exec_()) 