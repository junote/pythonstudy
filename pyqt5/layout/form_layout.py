from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QWidget, QPushButton,QHBoxLayout,QApplication,QVBoxLayout,QFormLayout,QLabel,QLineEdit

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform,self).__init__(parent)
        self.setWindowTitle("Form_Layout")


        flayout = QFormLayout()
        labl=[0] *3
        lEdit=[0]*3
        for i in range(3):
            labl[i] = QLabel(str(i))
            lEdit[i] = QLineEdit()
            flayout.addRow(labl[i], lEdit[i])
            
        self.setLayout(flayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hdemo= Winform()
    hdemo.show()
    sys.exit(app.exec_())