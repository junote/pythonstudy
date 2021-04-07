import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal

class Winform(QWidget):
    button_clicked_signal = pyqtSignal()

    def __init__(self,parent=None):
        super(Winform,self).__init__(parent)
        self.setWindowTitle("signal slot")
        self.resize(330,50)
        btn = QPushButton("close",self)
        btn.clicked.connect(self.btn_click)
        self.button_clicked_signal.connect(self.btn_close)

    def btn_click(self):
        self.button_clicked_signal.emit()
    
    def btn_close(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())