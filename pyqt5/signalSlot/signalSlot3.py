import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Winform(QWidget):
    def __init__(self,parent=None):
        super(Winform,self).__init__(parent)
        self.setWindowTitle("signal slot 3")
        self.resize(330,50)
        layout = QHBoxLayout()
        self.btn = QPushButton("OK",self)
        self.btn.setObjectName("okBtn")
        layout.addWidget(self.btn)
        self.setLayout(layout)
        QMetaObject.connectSlotsByName(self)

    @pyqtSlot()
    def on_okBtn_clicked(self):
        print("ok btn clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Winform()
    win.show()
    sys.exit(app.exec_())