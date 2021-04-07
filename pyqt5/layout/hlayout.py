from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QWidget, QPushButton,QHBoxLayout,QApplication,QVBoxLayout

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform,self).__init__(parent)
        self.setWindowTitle("HLayout")

        hlayout = QHBoxLayout()
        for i in range(6):
            hlayout.addWidget(QPushButton(str(i)))
        
        self.setLayout(hlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hdemo= Winform()
    hdemo.show()
    sys.exit(app.exec_())