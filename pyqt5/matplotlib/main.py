from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

from Ui_plt import Ui_Form

import sys


class MainWindow(QWidget, Ui_Form):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.widget.setVisible(False)
        self.widget_2.setVisible(False)
    
    @pyqtSlot()
    def on_pbtn_static_clicked(self):
        self.widget.setVisible(True)
        self.widget.mpl.start_static_plot()

    @pyqtSlot()
    def on_pbtn_dynamic_clicked(self):
        self.widget_2.setVisible(True)
        self.widget_2.mpl.start_dynamic_plot()   


if __name__ == '__main__' :

    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())