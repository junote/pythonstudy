from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QWidget, QPushButton,QHBoxLayout,QApplication,QVBoxLayout,QGridLayout

class Winform(QWidget):
    def __init__(self, parent=None):
        super(Winform,self).__init__(parent)
        self.setWindowTitle("GridLayout")
                
        names = [['cls', 'back', '', 'close'],
                 ['7','8','9','/'],
                 ['4','5','6','*'],
                 ['1','2','3','-'],
                 ['0','.','=','+']
                ]

        glayout = QGridLayout()
        for i in range(4):
            for j in range(4):
                glayout.addWidget(QPushButton(names[i][j]), i, j)
            
       
        self.setLayout(glayout)
        self.move(300,150)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hdemo= Winform()
    hdemo.show()
    sys.exit(app.exec_())