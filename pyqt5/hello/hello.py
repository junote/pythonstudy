from Ui_hello import *
import sys

if __name__ == "__main__":
    # pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    app = QtWidgets.QApplication(sys.argv)
    # QWidget部件是pyqt5所有用户界面对象的基类
    widget = QtWidgets.QWidget()
    # 导入配置文件
    ui = Ui_Form()
    # 关联配置文件和app
    ui.setupUi(widget)
    # 显示在屏幕上
    widget.show()
    #程序进入主循环。主循环会获取并分发事件。
    sys.exit(app.exec_())