from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QWidget, QPushButton,QHBoxLayout,QApplication,QVBoxLayout

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform,self).__init__(parent)
        self.setWindowTitle("VLayout")


        vlayout = QVBoxLayout()
        for i in range(6):
            vlayout.addWidget(QPushButton(str(i)))
            
        vlayout.addStretch(0)
        self.setLayout(vlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hdemo= Winform()
    hdemo.show()
    sys.exit(app.exec_())